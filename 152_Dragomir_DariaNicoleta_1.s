.data
 matrice: .space 1600
 matrice_iteratie: .space 1600
 m: .space 4
 n: .space 4
 p: .space 4
 k: .space 4
 parola: .space 1600
 criptaresaudecriptare: .space 4
 mesaj: .space 400
 cript: .space 1600
 nr: .long 0
 nr_concatenari: .space 400
 n2: .space 8
 m2: .space 8
 lungime_mesaj: .long 0
 lungime_mesaj_4: .long 0
 lungime_mesaj_8: .long 0
 lungime_cheie: .space 400
 lungime_cheie2: .space 800
 lineIndex: .space 4
 columnIndex: .space 4
 index: .space 4
 indexk: .space 4
 indexbinar: .space 4
 indexlitere: .space 4
 indexhex: .space 4
 indexi: .space 4
 indexj: .space 4
 left: .space 4
 right: .space 4
 formatScanf: .asciz "%d"
 formatScanfMesaj: .asciz "%s"
 formatPrintfMesaj: .asciz "%s\n"
 formatPrintfChar: .asciz "%c"
 formatPrintf: .asciz "%d"
 hex_afis: .asciz "0x"
 linienoua: .asciz "\n"
.text
.global main

main:
 pushl $m                   # nr. de linii
 pushl $formatScanf
 call scanf
 popl %ebx
 popl %ebx
 incl m
 incl m
 
 pushl $n                   # nr. de coloane
 pushl $formatScanf
 call scanf
 popl %ebx
 popl %ebx
 incl n
 incl n
 
 pushl $p                  # nr. de celule vii
 pushl $formatScanf
 call scanf
 popl %ebx
 popl %ebx
 movl $0,index
 
et_for:                    #aici se pun p 1-uri in matrice
 movl index,%ecx
 cmp %ecx,p
 je citire_k           

 pushl $left
 pushl $formatScanf
 call scanf
 popl %ebx
 popl %ebx

 pushl $right
 pushl $formatScanf
 call scanf
 popl %ebx
 popl %ebx
 
 incl left
 incl right
 
 movl m,%eax
 mull n
 movl %eax,lungime_cheie       #lungime cheie n*m
 
 movl left,%eax
 movl $0,%edx              #golesc edx ca sa nu impacteze rezultatul
 mull n
 addl right,%eax
 lea matrice,%edi
 lea matrice_iteratie,%esi     #matrice 2
 movl $1,(%edi,%eax,4)      #punem 1 pe matrice[left][right] -> left,right fiind cititi

 incl index
 jmp et_for

citire_k:
 pushl $k                  # nr. de iteratii
 pushl $formatScanf
 call scanf
 popl %ebx
 popl %ebx
 
 pushl $criptaresaudecriptare                  # alegerea tipului de rezolvare
 pushl $formatScanf
 call scanf
 popl %ebx
 popl %ebx
 
 pushl $mesaj                  # introducerea mesajului
 pushl $formatScanfMesaj
 call scanf
 popl %ebx
 popl %ebx

 movl $0,indexk
 jmp k_for
 
k_for:                    #prelucrare generatii
 movl indexk,%ecx
 cmp %ecx,k
 je criptdecript                      #criptdecript
 
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
   addl (%edi,%eax,4),%edx   #dreapta-jos   %edx are suma   
   subl $1,%eax 
   subl n,%eax            #ma intorc in centru
   
   cmp $0,%ebx                    #regulile jocului 0 si are 3 vecini => 1; <2 || >3 => 0; ==2/3=> 1
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

copiere:
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
   movl (%esi,%eax,4),%ebx
   movl %ebx,(%edi,%eax,4)
   
   incl columnIndex
   jmp for_columns_copiere
   
continuare_copiere:
  incl lineIndex
  jmp for_lines_copiere

mesajbinar:
  movl $0,indexlitere
  movl $mesaj,%edx
  lea parola,%ebp 
  movl $0,index
  jmp for_litere
  
for_litere: 
 movl indexlitere,%edi             #in edi repun matricea (cheia)
 cmp $10,%edi                       #cmp lungime_mesaj,%edi               
 je bag_lea

 movl $7,indexbinar
 
 incl indexlitere
 jmp for_binar 

for_binar:
  movl indexbinar,%ecx
  cmp $-1,%ecx
  je for_litere
  
  movl $1,%ebx
  movl $mesaj,%edx
  addl %edi,%edx
  movl (%edx),%eax         #112 in eax
  sall %ecx,%ebx         #(1<<index)
  			 #p => 01110000
  			 #     00000001
  cmp $0,%eax
  jne cresc_lungimea
  
continuare_binar:  			 
  andl %eax,%ebx
  cmp $0,%ebx
  
  jne afis_1
  jmp afis_0

cresc_lungimea:
 incl lungime_mesaj_8
 jmp continuare_binar  
 
afis_1: 
  movl $1,(%ebp)
  addl $4,%ebp
  
  decl indexbinar
  jmp for_binar
  
afis_0:
  movl $0,(%ebp)
  addl $4,%ebp
  
  decl indexbinar
  jmp for_binar

bag_lea:                             #calculez lungimea mesajului si numarul de concatenari
  lea parola,%ebp
  movl $0,%edx
  movl lungime_mesaj_8,%eax
  movl $8,%ebx
  divl %ebx
  movl %eax,lungime_mesaj
  
  movl $0,%edx
  movl lungime_mesaj_8,%eax
  movl lungime_cheie,%ebx
  divl %ebx
  movl %eax,nr_concatenari
  
  lea matrice, %edi
  addl lungime_cheie,%edi
  movl $0,index
  jmp for_nr_concatenari 
  
for_nr_concatenari:
 movl index,%ecx
 cmp nr_concatenari,%ecx
 je xor_start 
 concatenare_cheie:             #concatenez cheia
  movl $0,lineIndex
  for_lines_concatenare:
   movl lineIndex,%ecx
   cmp %ecx,m
   je continuare_nr_concatenari

   movl $0,columnIndex
   for_columns_concatenare:
    movl columnIndex,%ecx
    #addl $1,%ecx             matricea e bordata cu 0, dar afisam doar ce e inauntru
    cmp %ecx,n
    je continuare_concatenare

    movl lineIndex,%eax       #afisez cheia (%edi) => matrice
    movl $0,%edx
    mull n
    addl columnIndex,%eax
    lea matrice, %edi
    movl (%edi,%eax,4),%ebx
    addl lungime_cheie,%eax
    movl %ebx,(%edi,%eax,4)
  
    incl columnIndex
    jmp for_columns_concatenare
   
continuare_concatenare:                    
  incl lineIndex
  jmp for_lines_concatenare 

continuare_nr_concatenari:
 incl index
 jmp for_nr_concatenari  
                                # in xor_start il calculez pe cript
xor_start:
  lea parola,%ebp               # mesaj
  lea matrice,%edi              # cheie
  lea cript,%esi                # cript
  movl $0,index
  for_xor:
   movl index,%ecx
   cmp lungime_mesaj_8,%ecx
   je to_hex
   
   movl (%ebp,%ecx,4),%edx
   cmp %edx,(%edi,%ecx,4)
   je pun0_cript
    
   movl $1,(%esi,%ecx,4) 
   incl index
   jmp for_xor

pun0_cript:
  movl $0,(%esi,%ecx,4) 
  incl index
  jmp for_xor

criptdecript:
 movl criptaresaudecriptare,%ebx
 cmp $0,%ebx
 je mesajbinar               # il calculeaza pe cript si apoi afiseaza in hex
 jmp decriptare
 
to_hex:
  movl $4, %eax
  movl $1, %ebx
  movl $hex_afis, %ecx
  movl $2, %edx
  int $0x80
  movl $0,indexi
  movl $0,indexj
  lea cript,%esi             #in esi am cript
for_hex_i:
   movl indexi,%ecx
   cmp lungime_mesaj_8,%ecx
   je exit  
   
   movl $0,nr                
for_hex_j: 
    movl indexi,%ecx
    movl indexj,%edx
    addl $4,%ecx
    cmp %edx,%ecx
    je continuare_hex
    
    movl indexi,%ecx   #indexj e deja in edx
    subl %ecx,%edx    # j-i
    movl $3,%ebx
    movl %edx,%ecx     # j-i e in ecx
    subl %ecx,%ebx     
    movl %ebx,%ecx
    movl $1,%ebx
    sall %ecx,%ebx
    
    movl indexj,%edx       #a[j]
    movl (%esi,%edx,4),%eax
    mull %ebx       
    
    addl %eax,nr
    
    incl indexj
    jmp for_hex_j  
    
continuare_hex:
 addl $4,indexi
 movl nr,%ebx
 cmp $9,%ebx
 jg afis_hex
 pushl nr
    pushl $formatPrintf
    call printf
    popl %ebx
    popl %ebx
   
    pushl $0
    call fflush
    popl %ebx
 jmp for_hex_i  
   
afis_hex:
 addl $55,nr                     # adaug 'A' si scad 10
 pushl nr
    pushl $formatPrintfChar
    call printf
    popl %ebx
    popl %ebx
   
    pushl $0
    call fflush
    popl %ebx
 jmp for_hex_i    
 
decriptare: 
 movl $mesaj,%edx
 movl $2,index
 movl $0,%eax
 movl $0,lungime_mesaj
 lea cript,%esi
parcurgere_hex:
 movl index,%ecx
 movl $mesaj,%edx                
 addl %ecx,%edx
 movl $0,%ebx 
 movb (%edx,%ebx,1),%al            # ascii in al
 
 cmp $48,%eax                             # "\0" e 0 in ASCII, dar 0 e 48
 jl cript_hex
 
 cmp $64,%al
 jg e_litera
 sub $0,%al
 movl $0,indexk 

 for_hex_2_binar:
  movl $4,indexhex
  movl indexk,%ecx
  cmp $4,%ecx
  je continuare_cript_hex     #  0x70E1F26F6E63
  
  movl $1,%ebx
  andl %eax,%ebx

  cmp $0,%ebx
  je e_par
  jmp e_impar

e_par:                      
  pushl $0                        # folosesc stiva sa inversez elemente
  
  movl $1,%ecx
  movl %eax,%ebx
  sarl %ecx,%ebx                     # catul impartirii la 2(1 >> nr)
  movl %ebx,%eax
  incl indexk
  jmp for_hex_2_binar
e_impar:                      
  pushl $1
  movl $1,%ecx
  movl %eax,%ebx
  sarl %ecx,%ebx
  movl %ebx,%eax
  incl indexk
  jmp for_hex_2_binar  
e_litera: 
 sub $55,%al
 movl $0,indexk
jmp for_hex_2_binar 
continuare_cript_hex:
 popl (%esi)
 addl $4,%esi 
 popl (%esi)
 addl $4,%esi
 popl (%esi)
 addl $4,%esi
 popl (%esi)
 addl $4,%esi
 incl lungime_mesaj
 incl index
 jmp parcurgere_hex
 
cript_hex:
 movl lungime_mesaj,%eax   
 movl $4,%ebx
 mull %ebx
 movl %eax,lungime_mesaj_4
 movl $0,index
 lea cript,%esi
 for_afis_cript:
 movl index,%ecx
 cmp lungime_mesaj_4,%ecx

 jmp concat_cheie_decriptare  
  
concat_cheie_decriptare:
  lea cript,%esi
  
  movl $0,%edx
  movl lungime_mesaj_4,%eax
  movl lungime_cheie,%ebx
  divl %ebx
  movl %eax,nr_concatenari
  
  lea matrice, %edi
  addl lungime_cheie,%edi
  movl $0,index
  jmp for_nr_concatenari_hex 
  
for_nr_concatenari_hex:
 movl index,%ecx
 cmp nr_concatenari,%ecx
 je concatenare_hex                        #xor_start_hex
 concatenare_cheie_hex:             #concatenez cheia
  movl $0,lineIndex
  for_lines_concatenare_hex:
   movl lineIndex,%ecx
   cmp %ecx,m
   je continuare_nr_concatenari_hex

   movl $0,columnIndex
   for_columns_concatenare_hex:
    movl columnIndex,%ecx
    #addl $1,%ecx             matricea e bordata cu 0, dar afisam doar ce e inauntru
    cmp %ecx,n
    je continuare_concatenare_hex2

    movl lineIndex,%eax       #afisez cheia (%edi) => matrice
    movl $0,%edx
    mull n
    addl columnIndex,%eax
    lea matrice, %edi
    movl (%edi,%eax,4),%ebx
    addl lungime_cheie,%eax
    movl %ebx,(%edi,%eax,4)
  
    incl columnIndex
    jmp for_columns_concatenare_hex
   
continuare_concatenare_hex2:                    
  incl lineIndex
  jmp for_lines_concatenare_hex 

continuare_nr_concatenari_hex:
 incl index
 jmp for_nr_concatenari_hex   

concatenare_hex:
 lea matrice, %edi
 addl lungime_cheie,%edi
 
 movl lungime_cheie,%eax
 movl $2,%ebx
 mull %ebx
 movl %eax,lungime_cheie2
 
 movl n,%eax
 movl $2,%ebx
 mull %ebx
 movl %eax,n2
 
 movl m,%eax
 movl $2,%ebx
 mull %ebx
 movl %eax,m2
 
 movl $0,index
 jmp xor_decript 
 
xor_decript:
  lea parola,%ebp               # mesaj
  lea matrice,%edi              # cheie
  lea cript,%esi                # cript
  movl $0,index
  for_xor_decript:
   movl index,%ecx
   cmp lungime_mesaj_4,%ecx
   je binar_2_ascii
   
   movl (%edi,%ecx,4),%edx
   cmp %edx,(%esi,%ecx,4)
   je pun0_decript
    
   movl $1,(%ebp,%ecx,4) 
   incl index
   jmp for_xor_decript

pun0_decript:
  movl $0,(%ebp,%ecx,4) 
  incl index
  jmp for_xor_decript
binar_2_ascii:
  movl $0,indexi
  movl $0,indexj
  lea parola,%ebp             #in esi am cript
for_ascii_i:
   movl indexi,%ecx
   cmp lungime_mesaj_4,%ecx
   je exit  
   
   movl $0,nr                
for_ascii_j: 
    movl indexi,%ecx
    movl indexj,%edx
    addl $8,%ecx
    cmp %edx,%ecx
    je continuare_ascii
    
    movl indexi,%ecx   #indexj e deja in edx
    subl %ecx,%edx    # j-i
    movl $7,%ebx
    movl %edx,%ecx     # j-i e in ecx
    subl %ecx,%ebx     
    movl %ebx,%ecx
    movl $1,%ebx
    sall %ecx,%ebx
    
    movl indexj,%edx       #a[j]
    movl (%ebp,%edx,4),%eax
    mull %ebx       
    
    addl %eax,nr
    
    incl indexj
    jmp for_ascii_j  
    
continuare_ascii:
 addl $8,indexi
 movl nr,%ebx
 pushl nr
    pushl $formatPrintfChar
    call printf
    popl %ebx
    popl %ebx
   
    pushl $0
    call fflush
    popl %ebx
 jmp for_ascii_i   
exit:
 pushl $0
 call fflush
 addl $4, %esp

 movl $1,%eax
 xorl %ebx, %ebx
 int $0x80
