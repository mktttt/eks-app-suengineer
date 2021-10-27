#조건문을 시간, 명수 단계 


#request 로 받아와서 변수 뒤에 re를 붙여서 매개변수 이름을 정했음 
#차례 대로 사회적 거리두기 단계, 모임인원, 백신접종인원, 모임 시간 18시 이후여부 
def cal_moim(coronaWarninglevelGet,moimNGet,vaccineNGet):
    coronaWarninglevel=coronaWarninglevelGet
    moimN=moimNGet
    vaccineN=vaccineNGet
    
    
    try:
        if(coronaWarninglevel=='4'):
            MaxLimitN=8 
            MinLimitN=4
            moimN=int(moimN)
            vaccineN=int(vaccineN)   
            if(moimN<=MaxLimitN):
                if (moimN-vaccineN<=MinLimitN):                
                    return '모임 가능'
                else:
                    return '모임 불가능'
            else:
                return '모임 불가능'
        elif(coronaWarninglevel=='3'):
            MaxLimitN=10
            MinLimitN=4
            moimN=int(moimN)
            vaccineN=int(vaccineN)   
            if(moimN<=MaxLimitN):
                if (moimN-vaccineN<=MinLimitN):                
                    return '모임 가능'
                else:
                    return '모임 불가능'
            else:
                return '모임 불가능'
    
        elif(coronaWarninglevel=='2'):
            MaxLimitN=10
            moimN=int(moimN)
            vaccineN=int(vaccineN)   
            if(moimN<MaxLimitN):                
                return '모임 가능'
            else:
                return '모임 불가능'

        elif(coronaWarninglevel=='1'):   
            return  '방역수칙 준수하여 모임 권장 합니다(구체적 명수제한 X)'
        else:
            return '올바르게 입력해주세요'
    except:
        return '올바른 값을 입력해주세요'
    


