bunny = '''
          ,
            /|      __
           / |   ,-~ /
          Y :|  //  /
          | jj /( .^
          >-"~"-v"
         /       Y
        jo  o    |
       ( ~T~     j
        >._-' _./
       /   "~"  |
      Y     _,  |
     /| ;-"~ _  l
    / l/ ,-"~    \\
    \//\/      .- \\
     Y        /    Y    -Row
     l       I     !
     ]\      _\    /"\\
    (" ~----( ~   Y.  )
~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

piggy = '''
           9
     ,--.-'-,--.
     \  /-~-\  /
    / )' a a `( \\
   ( (  ,---.  ) )
    \ `(_o_o_)' /
     \   `-'   /
      | |---| |     hjw
      [_]   [_]
'''
while True:
    bunny_msg = input('Bunny: ')
    if bunny_msg == 'q':
        break
    print(bunny)
    print(bunny_msg)

    piggy_msg = input('Piggy: ')
    if piggy_msg == 'q':
        break
    print(piggy)
    print(piggy_msg)
