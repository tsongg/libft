import numpy as np
import matplotlib.pyplot as plt
import math
from math import exp, pi
import time
#########################################
## Runtime Check : Start ##
start = time.time()
## TOLERANCE ##
global reltol, vntol, abstol
reltol, vntol, abstol = 1e-3, 1e-3, 1e-6
#########################################
## R,L,C ##
global Rin, L, C
Rin = 450
L = 1e-6
C = 2e-12
## MOSFET ###
global lamda, beta, Vth, Rmos
lamda = 0.01
beta = 0.5 * 1e-3 # beta = myu_n * c_ox * W / L
Vth = 0.6
Rmos = 10000
## BJT ###
global af, ar, ies, ics, vtc, vte, Rbjt
af = 0.99
ar = 0.02
ies = 2e-14
ics = 99e-14
vtc = vte = 0.026
Rbjt = 640
## Diode ###
global isat, vt
isat, vt = 1e-12, 0.026
#########################################
## Simulation ##
global T, Vin_0
T = 30e-9
Vin_0 = 3 # Vin은 3V부터 시작
timestep = 0.1e-9 # 1e-10부터 정확
#timestep = 1e-12 # minimum timestep
#timestep = 1e-9 # 1e-9는 개형만 나옴
#########################################
## Code Flow 설명 ##
#
# 1. DC operating point를 구하는 Simulation 수행
# - NR_iteration_dcop 함수 / DcOp_SourceStepping 함수(DC sweep이라고 할 수 있음)
#
# 2. 1에서 나온 결과값을 초기값으로 Transient Simulation 수행
# - NR_iteration_transient 함수 / Transient_Simulation 함수
#
# 3. 나온 결과를 Plot
#
#########################################
## DC operating point Core 함수 ##
def NR_iteration_dcop(max_iteration, temp, v_1, v_3): # Newton-Raphson method

    # kth iteration loop
    while max_iteration :
        
        ############### Model Evaluation ################
        ## Model Equation을 k값이 업데이트 됨에 따라 새로 계산
        #-----------------------------------------------#
        ## BJT는 iteration에 따라 값이 변함 : k ##
        ## BJT : Ebers-Moll model ##
        vbek = temp[0] #v2k - GND
        vbck = temp[0] - temp[1] #v2k - v4k
        #-----------------------------------------------#
        geek = ies/vte * math.exp(vbek/vte)
        geck = ar * ics/vtc * math.exp(vbck/vtc)
        gcck = ics/vtc * math.exp(vbck/vtc)
        gcek = af * ies/vte * math.exp(vbek/vte)
        #-----------------------------------------------#
        iek = -ies*(math.exp(vbek/vte) - 1) + ar * ics*(math.exp(vbck/vtc) - 1)
        ick = af * ies*(math.exp(vbek/vte) - 1) - ics*(math.exp(vbck/vtc) - 1)
        Iek = iek + geek * vbek - geck * vbck
        Ick = ick - gcek * vbek + gcck * vbck
        #-----------------------------------------------#

        ## MOSFET은 iteration에 따라 값이 변함 : k ##
        ## MOSFET : simple quadratic DC model (suitable for long channel devices)##
        global gdsk,id_k,gmk
        vgsk = temp[1] #v4k - GND
        vdsk = temp[2] #v5k - GND
        #-----------------------------------------------#
        ## linear region ## 0 <= vdsk <= vgsk - Vth
        if 0 <= vdsk and vdsk < vgsk - Vth :
            gdsk = beta * (vgsk - vdsk - Vth)
            gmk = beta * vdsk
            id_k = beta * ((vgsk - Vth)*vdsk - (vdsk **2)/2)
        #-----------------------------------------------#
        ## satuation region ## 0 <= vgsk - Vth <= vdsk
        elif 0 < vgsk - Vth and vgsk - Vth <= vdsk :
            gdsk = beta / 2 * lamda * (vgsk - Vth)**2
            gmk = beta * (vdsk - Vth) * (1 + lamda * vdsk)
            id_k = beta / 2 * (vgsk - Vth)**2 * (1 + lamda * vdsk)
        #-----------------------------------------------#
        ## cutoff region ## vgsk <= Vth
        elif vgsk <= Vth :
            gdsk = 0
            gmk = 0
            id_k = 0
        #-----------------------------------------------#
        ieqk = id_k - gdsk * vdsk - gmk * vgsk
        #-----------------------------------------------#

        ## Diode는 iteration에 따라 값이 변함 : k ##
        #vdk = v_plus - v_minus
        #geqk = isat*math.exp(vdk/vt) / vt
        #-----------------------------------------------#

        ## NA matrix 풀기 ##
        #-----------------------------------------------#
        # element stamp를 이용해서 3by3 NA matrix 생성
        a = np.array( [ 
            [ gcck+geek-gcek-geck+1/Rin  , geck-gcck   , 0 ] ,
            [ gcek-gcck                  , gcck+1/Rbjt , 0 ] , 
            [ 0                          , gmk         , gdsk+1/Rmos ] ] )
        b = np.array( 
            [ Iek+Ick+(v_1)/Rin              , -Ick+(v_3)/Rbjt , -ieqk+(v_3)/Rmos ] ) # RHS Vector에서 Source 전압값을 키워준다
        # np.linalg.inv 알고리즘 : LU Decompositon 후 forward, backward substitution 수행
        x = np.linalg.inv(a) @ b
        #-----------------------------------------------#

        # 순서대로 v2k, v4k, v5k
        d = np.array( [
            x[0] , # v2k
            x[1] , # v4k
            x[2]   # v5k
            ] )
        
        # 작업시 log 확인
        print("Dc op iter : v2k =",d[0]," v4k =",d[1]," v5k =",d[2])

        if abs(temp[0]-d[0]) < vntol and\
            abs(temp[1]-d[1]) < vntol and\
                abs(temp[2]-d[2]) < vntol :
            break
        else :
            temp = d
            max_iteration -= 1
    
    # i 는 따로 계산
    ic_bjt_n = 0
    ic_mos_n = 0
    il_n = ((v_3)-d[1])/Rbjt + ((v_3)-d[2])/Rmos #v3-v4 / Rbjt + v3-v5 / Rmos

    # 결과 array, 순서대로 (t,vin), (v2, v3, v4, v5), (ic_bjt_n, ic_mos_n, il_n)
    resarr = np.array( [ 0,v_1, d[0],v_3,d[1],d[2], ic_bjt_n,ic_mos_n,il_n ] ).T

    # 출력값 : iniarray : DC_OP로 얻은 초기값
    return resarr
#---------------------------------------#
## DC operating point Souce Stepping 함수 ##
def DcOp_SourceStepping(max_iteration):
    # initial guessing, Dc voltage의 값을 step up 하며 nonconverge를 피한다

    ## Souce Stepping ##
    v_1 = 0 # 목표 3V
    v_3 = 0 # 목표 3V
    increment = 0.1

    # 초기값 v2, v4, v5 = 0,0,0 부터 시작
    temp = np.array( [ 0 , 0 , 0 ] )

    while v_1 <= Vin_0 and v_3 <= 3 :
        v_1 += increment
        v_3 += increment

        temparr = NR_iteration_dcop(max_iteration, temp, v_1, v_3)
        # temp 값 update
        temp = np.array( [ temparr[2] , temparr[4] , temparr[5] ] )
    
    return temparr
#########################################
#########################################
## Transient Simulation 함수 ##
def NR_iteration_transient(ini, Vin, dt): # Newton-Raphson method
    # temp 초기값
    temp = ini

    ## LC는 n-1의 값을 사용(이전 timepoint에서의 값) ##
    ## L,C ## : Trapazoidal Rule
    #-----------------------------------------------#
    geq_c_bjt = 2*C/dt
    geq_c_mos = 2*C/dt
    ieq_c_bjt = geq_c_bjt*ini[2] + ini[4] #v4k
    ieq_c_mos = geq_c_mos*ini[3] + ini[5] #v5k
    #-----------------------------------------------#
    geq_l = dt/(2*L)
    ieq_l = geq_l*(3-ini[1]) + ini[6] #v3k
    #-----------------------------------------------#

    # max iteration을 제한
    max_iteration = 20

    # iteration counting
    i = 1

    # kth iteration loop
    while i <= max_iteration-1 :
        
        ############### Model Evaluation ################
        ## Model Equation을 k값이 업데이트 됨에 따라 새로 계산
        #-----------------------------------------------#
        ## BJT는 iteration에 따라 값이 변함 : k ##
        ## BJT : Ebers-Moll model ##
        vbek = temp[0] #v2k - GND
        vbck = temp[0] - temp[2] #v2k - v4k
        #-----------------------------------------------#
        geek = ies/vte * math.exp(vbek/vte)
        gcck = ics/vtc * math.exp(vbck/vtc)
        gcek = af * ies/vte * math.exp(vbek/vte)
        geck = ar * ics/vtc * math.exp(vbck/vtc)
        #-----------------------------------------------#
        iek = -ies * (math.exp(vbek/vte) - 1) + ar * ics * (math.exp(vbck/vtc) - 1)
        ick = af * ies * (math.exp(vbek/vte) - 1) - ics * (math.exp(vbck/vtc) - 1)
        Iek = iek + geek * vbek - geck * vbck
        Ick = ick - gcek * vbek + gcck * vbck
        #-----------------------------------------------#

        ## MOSFET은 iteration에 따라 값이 변함 : k ##
        ## MOSFET : simple quadratic DC model (suitable for long channel devices)##
        global gdsk,id_k,gmk
        vgsk = temp[2] #v4k - GND
        vdsk = temp[3] #v5k - GND
        #-----------------------------------------------#
        ## linear region ## 0 <= vdsk <= vgsk - Vth
        if 0 <= vdsk and vdsk < vgsk - Vth :
            gdsk = beta * (vgsk - vdsk - Vth)
            gmk = beta * vdsk
            id_k = beta * ((vgsk - Vth)*vdsk - (vdsk **2)/2)
        #-----------------------------------------------#
        ## satuation region ## 0 <= vgsk - Vth <= vdsk
        elif 0 < vgsk - Vth and vgsk - Vth <= vdsk :
            gdsk = beta / 2 * lamda * (vgsk - Vth)**2
            gmk = beta * (vdsk - Vth) * (1 + lamda * vdsk)
            id_k = beta / 2 * (vgsk - Vth)**2 * (1 + lamda * vdsk)
        #-----------------------------------------------#
        ## cutoff region ## vgsk <= Vth
        elif vgsk <= Vth :
            gdsk = 0
            gmk = 0
            id_k = 0
        #-----------------------------------------------#
        ieqk = id_k - gdsk * vdsk - gmk * vgsk
        #-----------------------------------------------#

        ## Diode는 iteration에 따라 값이 변함 : k ##
        #vdk = v_plus - v_minus
        #geqk = isat*math.exp(vdk/vt) / vt
        #-----------------------------------------------#

        ## MNA matrix 풀기 ##
        """
        #Ax=B 풀기
        A = np.array( [ 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] ] )
        B = np.array( 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] )
        """
        # Element stamp를 이용해서 7by7 MNA matrix 생성
        # branch current 항 : dynamic element가 있는 부분은 필수적으로 구해야 한다
        # 생성하는 공식 설명 > PPT
        A = np.array( [
            [ gcck+geek-gcek-geck+1/Rin , 0                   , geck-gcck             , 0                     ,          0 ,          0 , 0 ] ,
            [ 0                         , 1/Rbjt+1/Rmos+geq_l , -1/Rbjt               , -1/Rmos               ,          0 ,          0 , 0 ] ,
            [ gcek-gcck                 , -1/Rbjt             , gcck+1/Rbjt+geq_c_bjt , 0                     ,          0 ,          0 , 0 ] , 
            [ 0                         , -1/Rmos             , gmk                   , gdsk+1/Rmos+geq_c_mos ,          0 ,          0 , 0 ] ,
            [ 0                         , 0                   , -geq_c_bjt            , 0                     ,          1 ,          0 , 0 ] ,
            [ 0                         , 0                   , 0                     , -geq_c_mos            ,          0 ,          1 , 0 ] ,
            [ 0                         , geq_l               , 0                     , 0                     ,          0 ,          0 , 1 ] ] )
        B = np.array(
            [ Iek+Ick+Vin/Rin           , 3*geq_l+ieq_l       , ieq_c_bjt-Ick         , ieq_c_mos-ieqk        , -ieq_c_bjt , -ieq_c_mos , 3*geq_l+ieq_l ] )
        # np.linalg.inv 알고리즘 : LU Decompositon 후 forward, backward substitution 수행
        # 순서대로 v2k, v3k, v4k, v5k, ic_bjt_k, ic_mos_k, il_k
        x = np.linalg.inv(A) @ B
        #-----------------------------------------------#

        d = np.array( [ 
            x[0] ,  # v2k
            x[1] ,  # v3k
            x[2] ,  # v4k
            x[3] ,  # v5k
            x[4] ,  # ic_bjt_k
            x[5] ,  # ic_mos_k
            x[6] ] )# il_k

        # 작업시 log 확인
        #print(d)

        # iteration stop 기준, k와 k+1 의 차이가 이것보다 작으면 stop
        # nodevoltage
        stop0 = abs(reltol*ini[0]) + vntol
        stop1 = abs(reltol*ini[1]) + vntol
        stop2 = abs(reltol*ini[2]) + vntol
        stop3 = abs(reltol*ini[3]) + vntol
        # branchcurrent
        stop4 = abs(reltol*ini[4]) + abstol
        stop5 = abs(reltol*ini[5]) + abstol
        stop6 = abs(reltol*ini[6]) + abstol

        if abs(d[0]-temp[0]) < stop0 and abs(d[1]-temp[1]) < stop1 and\
                abs(d[2]-temp[2]) < stop2 and abs(d[3]-temp[3]) < stop3 and\
                        abs(d[4]-temp[4]) < stop4 and abs(d[5]-temp[5]) < stop5 and\
                                abs(d[6]-temp[6]) < stop6 : # all node, current 조건충족
            break
        else: # keep going
            temp = d
            i += 1

    # NR converge된 nodevoltage, branchcurrent의 값을 반환한다
    return d , dt , i
#---------------------------------------#
# 입력값 : iniarray : DC_OP로 얻은 초기값이 들어간다.
def Transient_Simulation(dcop_result): # Dynamic timestep control : iteration counting method

    # 초기값 설정 >> perform DC Analysis, 0일때의 초기값을 먼저 구해둔다
    resarr = np.array(
        [[dcop_result[0]] , [dcop_result[1]] , # t,vin
        [dcop_result[2]] , [dcop_result[3]] , [dcop_result[4]] , [dcop_result[5]] , # v2, v3, v4, v5
        [dcop_result[6]] , [dcop_result[7]] , [dcop_result[8]]]) # ic_bjt_n, ic_mos_n, il_n

    # 각각의 timepoint에서 결과값 저장 array
    converge = np.array([ 
        dcop_result[2] , dcop_result[3] , dcop_result[4] , dcop_result[5] , # v2, v3, v4, v5
        dcop_result[6] , dcop_result[7] , dcop_result[8] ]).T # ic_bjt_n, ic_mos_n, il_n
    
    # 초기값
    dt = timestep
    t = dt
    n = 0

    while t <= T :

        # NR 수행 update
        Vin = Vin_0 * math.exp(-t/2e-9)
        converge, dt, i = NR_iteration_transient(converge, Vin, dt)

        # iteration 횟수가 20 이상이면 dt를 절반으로 줄여서 다시 계산을 진행
        if i == 20 : 
            converge, dt ,i = NR_iteration_transient(converge, Vin, dt/2)

        # 결과값 저장 순서대로 (t,vin), (v2, v3, v4, v5), (ic_bjt_n, ic_mos_n, il_n)
        adddata = np.array([[t],[Vin],
        [converge[0]],[converge[1]],[converge[2]],[converge[3]],
        [converge[4]],[converge[5]],[converge[6]]])
        resarr = np.append(resarr, adddata, axis=1)

        # t, point 업데이트
        t += dt
        n += 1
        
        # 작업시 log 확인
        #print(t, dt, n, i)

        # dynamic timestep 적용 _ iteration counting method
        if i >= 10 : # i가 10 이상이면 다음 dt를 절반으로 줄인다
            dt = dt / 2
            if dt > 1e-3 : dt = 1e-3
            elif dt < 1e-12 : dt = 1e-12

        elif i <= 1 : # i가 1 이하이면 다음 dt를 두배로
            dt = dt * 2
            if dt > 1e-3 : dt = 1e-3
            elif dt < 1e-12 : dt = 1e-12

    return resarr
#########################################
#########################################
## Simulation 수행 ##
iniarray = DcOp_SourceStepping(30) # Dc Operating point
sim = Transient_Simulation(iniarray) # Transient Simulation
xt = sim[0,:]
vin = sim[1,:]
#v2 = sim[2,:]
#v3 = sim[3,:]
v4 = sim[4,:]
v5 = sim[5,:]
#icbjt = sim[6,:]
#icmos = sim[7,:]
#icl = sim[8,:]
#########################################
## Runtime Check : End ##
end = time.time()
print(f"Runtime : {end - start:.5f} sec")
#########################################
## Graph plot ##
plt.scatter(xt, vin, s=1.5, label = 'vin')
plt.scatter(xt, v4, s=1.5, label = 'v4')
plt.scatter(xt, v5, s=1.5, label = 'v5')
#plt.plot(xt, vin, label = 'vin')
#plt.plot(xt, v4, label = 'v4')
#plt.plot(xt, v5, label = 'v5')

plt.title('Transient Simulation', fontsize=14)
plt.xlabel('Time(sec)', fontsize=12)
plt.ylabel('Voltages(V)', fontsize=12)

plt.legend() # 범례 표시
plt.grid(True, linestyle='--') # grid 표시

plt.show()
#########################################