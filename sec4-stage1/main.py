import json
#로그 파일을 읽는 함수
def print_log(path_log):
    # try : 오류가 발생할 수 있는 코드 작성:
    try:
        # with: 설정 및 정리 작업을 자동으로 처리하여 리소스 관리를 간소화 
        # as : 반환된 객체를 변수에 할당
        with open(path_log, 'r',encoding="utf-8") as log_file:
            log_file = log_file.read()
            print(log_file) #자동으로 파일이 닫음
    #except : try블록에서 특정 예외가 발생시 실행할 코드 작성
    except FileNotFoundError as err:
        print("EN: There should be a misstion_computer_main.log file in that path.")
        print("KR: 해당 경로의 mission_computer_main.log 파일이 있어야 합니다.")
        print(f"에러 출력 :{err}")
    except UnicodeDecodeError as err:
        print(f"디코딩 중 에러 발생 :{err}")
        print(f"해당파일:{path_log} open메소드의 인코딩 형식과 맞는지 확인")
        print(f"명령어 : file -ib {path_log}")

# 파일을  반복자로 읽기 
def iter_log(path_log, list_log):
    try:
        with open (path_log,'r',encoding='utf-8') as lines:
            for line in lines:
                list_log.append(line.strip().split(","))
        return list_log
    #except : try블록에서 특정 예외가 발생시 실행할 코드 작성
    except FileNotFoundError as err:
        print("EN: There should be a misstion_computer_main.log file in that path.")
        print("KR: 해당 경로의 mission_computer_main.log 파일이 있어야 합니다.")
        print(f"에러 출력 :{err}")
    except UnicodeDecodeError as err:
        print(f"디코딩 중 에러 발생 :{err}")
        print(f"해당파일:{path_log} open메소드의 인코딩 형식과 맞는지 확인")
        print(f"명령어 : file -ib {path_log}")


#배열을 역순으로 정렬
def sort_log(list_log):
    list_log.sort(reverse=True)
    return list_log

def dict_log(list_log):
    #1행들은 키값으로 반영 
    dict_keys = dict.fromkeys(list_log[0])
    dict_list =[]
    #keys에 대한 전체 출력 값 
    print(dict_keys)
    #해당 키에 대한 값만 출력 
    print(dict_keys["timestamp"])
    
    # 반복해서 배열의 해당 키,값 넣기
    for i in range(1,len(list_log)):
        dict_keys["timestamp"] = list_log[i][0]
        dict_keys["event"] = list_log[i][1]
        dict_keys["message"] = list_log[i][2]
        
        dict_list.append(dict_keys.copy())
    return dict_list 

# list의 데이터를 배열로 저장
def json_file(list_log,json_name):
    try:
        with open(json_name,"w",encoding="utf-8") as w_json:
            json.dump(list_log,w_json)
	
    except UnicodeDecodeError as err:
        print(f"디코딩 중 에러 발생 :{err}")
        print(f"해당파일:{path_log} open메소드의 인코딩 형식과 맞는지 확인")
        print(f"명령어 : file -ib {path_log}")


def main():
    print_log("./mission_computer_main.log")
    
    print("")
    print("")
    print("")
    print("===iter_log 함수실행===")

    list_log=[]
    list_log = iter_log("./mission_computer_main.log",list_log)
    for i in range(0,int(len(list_log)/2)):
        print(list_log[i])

    print("")
    print("")
    print("")
    print("===sort_log 함수 실행===")
    list_log = sort_log(list_log)
    for i in range(0, int(len(list_log) / 2)):
        print(list_log[i])
    
    print("")
    print("")
    print("")
    print("===dict_log 함수 실행===")
    list_log = dict_log(list_log)
    print(list_log)
    for i in range(0, int(len(list_log) / 2)):
        print(list_log[i])


    print("")
    print("")
    print("")
    print("===json_file 함수 실행===")
    list_log = json_file(list_log,"mission_computer_main.json")

    print("===EXIT===")

if __name__ == "__main__":
    main()                    
