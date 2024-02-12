.data
 matrice: .space 1600
 matrice_iteratie: .space 1600
 m: .space 4
 n: .space 4
 p: .space 4
 k: .space 4
 lineIndex: .space 4
 columnIndex: .space 4
 index: .space 4
 indexk: .space 4
 left: .space 4
 right: .space 4
 formatScanf: .asciz "%d"
 formatPrintf: .asciz "%d "
 linienoua: .asciz "\n"
 
 #fisiere citire afisare
 inputFile: .asciz "in.txt"
 outputFile: .asciz "out.txt"
 read: .asciz "r"
 write: .asciz "w"
 filer: .long 0
 filew: .long 0
 
 
.text
.global main

main:
 #deschid fisierul pt. citire
 push $read
 push $inputFile
 call fopen
 mov %eax, filer
 add $8, %esp  
    
 #deschid fisierul pt. afisare
 push $write
 push $outputFile
 call fopen
 mov %eax, filew
 add $8, %esp 

 lea m, %eax     #nr. de linii 
 push %eax
 push $formatScanf
 push filer
 call fscanf
 add $12, %esp
 incl m
 incl m
 
 lea n, %eax      #nr. de coloane
 push %eax
 push $formatScanf
 push filer
 call fscanf
 add $12, %esp
 incl n
 incl n
 
 lea p, %eax        #nr. celule vii
 push %eax
 push $formatScanf
 push filer
 call fscanf
 add $12, %esp
 
 movl $0,index
 
et_for:                    #aici se pun p 1-uri in matrice
 movl index,%ecx
 cmp %ecx,p
 je citire_k           

 lea left, %eax      #linie
 push %eax
 push $formatScanf
 push filer
 call fscanf
 add $12, %esp

 lea right, %eax     #coloana
 push %eax
 push $formatScanf
 push filer
 call fscanf
 add $12, %esp
 
 incl left
 incl right
 
 movl left,%eax
 movl $0,%edx              #golesc edx ca sa nu impacteze rezultatul
 mull n
 addl right,%eax
 lea matrice,%edi
 lea matrice_iteratie,%esi     #matrice 2
 movl $1,(%edi,%eax,4)      #punem 1 pe matrice[left][right] -> left,right fiind cititi de la tastatura

 incl index
 jmp et_for

citire_k:
 lea k, %eax     #nr. de iteratii 
 push %eax
 push $formatScanf
 push filer
 call fscanf
 add $12, %esp
 
 movl $0,indexk
 jmp k_for
 
k_for:                    #prelucrare generatii
 movl indexk,%ecx
 cmp %ecx,k
 je afisare_matrice
 
 movl $1,lineIndex
 for_lines_k:
  movl lineIndex,%ecx
  cmp %ecx,m
  je copiere

  movl $1,columnIndex
  for_columns_k:
   movl columnIndex,%ecx
   addl $1,%ecx              
   cmp %ecx,n
   je continuare_k

   movl lineIndex,%eax       
   movl $0,%edx
   mull n
   addl columnIndex,%eax
   lea matrice, %edi
   movl (%edi,%eax,4),%ebx   # vecinii
   
   subl n,%eax               #sus
   addl (%edi,%eax,4),%edx
   subl $1,%eax              #stanga-sus
   addl (%edi,%eax,4),%edx
   addl $2,%eax              #dreapta-sus
   addl (%edi,%eax,4),%edx
   addl n,%eax
   addl (%edi,%eax,4),%edx   #dreapta
   subl $2,%eax
   addl (%edi,%eax,4),%edx   #stanga
   addl n,%eax
   addl (%edi,%eax,4),%edx   #stanga-jos
   addl $1,%eax
   addl (%edi,%eax,4),%edx   #jos
   addl $1,%eax
   addl (%edi,%eax,4),%edx   #dreapta-jos   %edx are suma   0 si are 3 vecini => 1; <2 || >3 => 0; ==2/3=> 1
   subl $1,%eax 
   subl n,%eax            #ma intorc in centru
   
   cmp $0,%ebx                #regulile jocului
   je e_zero
   
   cmp $2,%edx
   jl devine_0
   
   cmp $2,%edx
   je devine_1
   
   cmp $3,%edx
   jg devine_0
   
   jmp devine_1
  
e_zero:
   cmp $3,%edx
   je devine_1
   jmp continuare_coloane_k
   
devine_1:
   movl $1,(%esi,%eax,4)
   je continuare_coloane_k
   
devine_0:
   movl $0,(%esi,%eax,4)
   je continuare_coloane_k
   
continuare_coloane_k:
   incl columnIndex
   jmp for_columns_k
   
continuare_k:
  incl lineIndex
  jmp for_lines_k
 
iteratie_k:
 incl indexk
 jmp k_for

copiere:                        #copiez matricea cu schimbarile necesare dupa fiecare iteratie in cea principala
 movl $1,lineIndex
 for_lines_copiere:
  movl lineIndex,%ecx
  cmp %ecx,m
  je iteratie_k

  movl $1,columnIndex
  for_columns_copiere:
   movl columnIndex,%ecx
            
   cmp %ecx,n
   je continuare_copiere

   movl lineIndex,%eax       #copiaza matricea
   movl $0,%edx
   mull n
   addl columnIndex,%eax
   movl (%esi,%eax,4),%ebx      #matrice_iteratie -> %esi
   movl %ebx,(%edi,%eax,4)      #matrice -> %edi
   
   incl columnIndex
   jmp for_columns_copiere
   
continuare_copiere:
  incl lineIndex
  jmp for_lines_copiere
 
afisare_matrice:
 movl $1,lineIndex
 decl m
 for_lines:
  movl lineIndex,%ecx
  cmp %ecx,m
  je exit

  movl $1,columnIndex
  for_columns:
   movl columnIndex,%ecx
   addl $1,%ecx              #matricea e bordata cu 0, dar afisam doar ce e inauntru
   cmp %ecx,n
   je continuare

   movl lineIndex,%eax       #afisez matricea[lineIndex][columnIndex]
   movl $0,%edx
   mull n
   addl columnIndex,%eax
   lea matrice, %edi
   movl (%edi,%eax,4),%ebx
   

   pushl %ebx
   pushl $formatPrintf
   push filew
   call fprintf
   add $12, %esp

   pushl $0
   call fflush
   popl %ebx

   incl columnIndex
   jmp for_columns
   
 continuare:
   pushl $linienoua
   push filew
   call fprintf
   add $12, %esp

   pushl $0
   call fflush
   popl %ebx
  incl lineIndex
  
  jmp for_lines

exit:
 push filer
 call fclose
 add $4, %esp 

 push filew
 call fclose
 add $4, %esp 

 pushl $0
 call fflush
 addl $4, %esp

 movl $1,%eax
 xorl %ebx, %ebx
 int $0x80
