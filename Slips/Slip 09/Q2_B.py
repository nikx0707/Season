def palindrome(n) :

    temp = n

    rev = 0

    while n>0:

        dig = n%10

        rev = rev *10 + dig

        n = n //10

        if temp == rev:

            print(temp,"The Number is a Palindrome !")

        else :

            print(temp,"The Number isn't a Palindrome !")



        def armstrong(n):

            count =0

            temp = n

            while temp>0:

                digit =temp %10

                count += digit **3

                temp//=10

            if(n==count):

                print(n, "is an Armstrong Number")

            else:

                print(n, "is not an Armstrong Number")



        def perfect(n):

            count=0

            for i in range(1,n):

                if n % i==0:

                    count = count +i

            if count ==n:

                print(n,"The Number is a Perfect Number !")

            else :

                print(n,"The Number is Not a Perfect Number !")

        

        if __name__ == '__main__':

            n = int(input("Enter Number : "))

            palindrome(n)

            armstrong(n)


            perfect(n)

