## 중첩 for문을 이용한 구구단
for i in range(1,10):
    print(f"<{i}단> \n")
    for j in range(1,10):
        print(f"{i}x{j} = {i*j}")
    print("---------")
print("감사합니다 :)")