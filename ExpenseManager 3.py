
expense=[]

#----------ثبت هزنینه---------------

def AE() :
    while True:
        print()
        name1=input("what do you buy : ").strip()
        if len(name1) >= 100:
            print("your name has a lot of words !!!")
            return
        else:
            if name1=='':
                print("give me something !")
                return
            else:

                try:
                    print()
                    cost1=float(input("haw much does it cost : "))
                    if cost1 >= 0 :
                        print()
                        category1=input("what was it about : ").strip()
                        if len(category1)<=100:
                            if category1!="":
                                dic = {"title":name1,"costs":cost1,"categorys":category1}
                                expense.append(dic)
                                print("it added succesfully!")
                                restart=input("do you want to add another one (y/n) ?").strip().lower()
                                if restart=="yes" or restart=='y':
                                    continue
                                else:
                                    if restart=="n" or restart=='no':
                                        break
                                        return
                                    else:
                                        print("choose between them !")
                                        return
                            else:
                                print("give me something !")
                                return
                        else:
                            print("your category has a lots of word !!!")
                            return
                    else:
                        print("something is wrong with your expense !")
                        return
                except ValueError:
                    print("give me number !")
                except Exception as e:
                    print(F'ERROR : {e}')



#تمام هزینه ها --------------
def show():
    if expense != []:
        print()
        for a in expense :
            print(a['title'],"---",a['costs'],"---",a['categorys'])
    else:
        print("We have nothing to show ...")
        return

        
#=============پیدا کردن بیشترین هزینه
def maxE(expense):
    if len(expense)!=0:
        m = expense[0]
        for cost in expense :
            if cost['costs'] > m['costs'] :
                m = cost
        if 'categorys' in m :
            print(m['title'],'---',m['costs'],'---',m['categorys'])
            return
        else:
            m.get('categorys')
            print(m['title'],'---',m['costs'],'---',m['categorys'])
            return

    else:
        print("there is nothing ...")
        return


#؟؟؟؟؟؟؟؟؟؟جستوجوی هزینه؟؟؟؟؟؟؟؟؟

def SE():
    if len(expense) > 0 :
        num = input("give me title that you want to see :").strip().lower()
        found = []
        for n in expense:
            if n["title"].strip().lower() == num:
                found.append(n)

        if len(found) == 0:
            print("nothing found!")
            return

        for ex in found:
            print(ex["title"], "---", ex["costs"], "---", ex["categorys"])
    else:
        print("no number to search !")
        return



                
        
            
#______________حذف هزینه_________

def DE():
    while True:
        if len(expense) != 0 :
            
            u = input("tell me your title to delete :").lower().strip()
            founded=[]
            for n in expense:
                if n['title']==u:
                    founded.append(n)
                    
            try:

                if len(founded)==0:
                    print("nothing find !")
                    return
                elif len(founded)==1:
                    del expense[expense.index(founded[0])]
                    print("succesfully Deleted !")
                    restart=input("do you want to delete another thing (y/n) ?").strip().lower()
                    if restart=="yes" or restart=='y':
                        continue
                    else:
                        if restart=="n" or restart=='no':
                            break
                            return
                        else:
                            print("choose between them !")
                            return
                    
                    

                elif len(founded)>=2:
                    print(F"what we found : ")
                    for e in founded:
                        print(e['title'],'---',e['costs'],'---',e['categorys'])
                    print()
                    shab=int(input("which one do you want to delete(number):"))
                    
                    if len(founded) >= shab and shab >0:
                        del expense[expense.index(founded[0])-1]
                        print("deleted succesfully !")
                        restart=input("do you want to add another one (y/n) ?").strip().lower()
                        if restart=="yes" or restart=='y':
                            continue
                        else:
                            if restart=="n" or restart=='no':
                                break
                                return
                            else:
                                print("choose between them !")
                                return
                    else:
                        print("choose between them !")
                        return
            except ValueError:
                print("try again!")
            except Exception as e :
                print(F'ERROR : {e}')
        else:
            print("no number to delete !")
            return





#:::::::::::::منو اصلی::::::::::::
def ExpenseManager():
    while True :
        print("1.Add an expense .")
        print("2.Show all expense .")
        print("3.calculate Total expense .")
        print("4.Search Expense .")
        print("5.Delete expense .")
        print("6.Show most expense .")
        print("7.Exit .")
        print()
        choise=input("what do you need to do : ").strip()


        if choise in ('1','2','3','4','5','6','7'):


            if choise == '1' :
                AE()
                print("-"*20)

            elif choise == '2' :
                print()
                show()
                print("-"*20)


            elif choise == '3' :
                if expense !=[]:
                    print(sum(d['costs'] for d in expense))
                    print("-"*20)
                else:
                    print("We have nothing to calculate ...")


            elif choise == '4' :
                print()
                SE()
                print("-"*20)


            elif choise == '5' :
                print()
                DE()
                print("-"*20)


            elif choise == '6' :
                print()
                maxE(expense)
                print("-"*20)

            elif choise == '7' :
                print("👋 Goodbye ")
                break


        else:
            print("choose between the number !")

if __name__ == "__main__":
    ExpenseManager()