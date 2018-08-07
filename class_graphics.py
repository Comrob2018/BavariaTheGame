
class Art:
  def __init__(self, pname, pnumparts, pparts=[]):
        self.artName = pname
        self.parts = pnumparts
        self.lines = pparts

  def AddLine(self,ppart):
    self.lines.append(ppart)
    self.parts += 1

  def ShowArt(self):
        for x in range(0, self.parts - 1):
            print(self.lines[x])

class Graphics_Engine:
  def __init__(self, pname, pnumparts, pparts=[]):
        self.artList = []
        self.currentGraphic = ''

  def SetCurrentGraphic(self, pname):
    self.currentGraphic = pname

  def TPrint(self, p_graphics_string, pname=""):
    if pname == "":
      pname = self.currentGraphic
    if (self.CallArtByName(pname) == False):
      self.AddArt(1,p_graphics_string)
    else:
      self.CallArtByName(pname).AddLine(p_graphics_string)

  def AddArt(self, pname, pnumparts, pparts=[]):
    self.artList.append(Art(pname))

  def CallArtByName(self, pname):
      for a in self.artList:
          if a.artName == pname:
              return a
      return False

  def CallArtByID(self, pID):
    return self.artList[pID]

  #Graphics init
  def InitImages(self):
    self.SetCurrentGraphic("Cave_Enter")
    self.Tprint('')
    self.Tprint('You found the entrance to the cave!')
    self.Tprint('')
    self.Tprint('........................../\...../####\ ')
    self.Tprint('../\./\.....__________...//\\\.../###### ')
    self.Tprint(' //\\\/\\\.../  *       \...||.../####### ')
    self.Tprint('.//\\\||.../       *    \....../######## ')
    self.Tprint('..||...../  *   *       \..../######### ')
    self.Tprint('......../       __   *   \../########## ')
    self.Tprint('......./    *  /##\       \....../\.... ')
    self.Tprint('....../  *    |####|   *   \....//\\\... ')
    self.Tprint('...../________|####|________\...//\\\... ')
    self.Tprint('.................................||.... ')

    self.SetCurrentGraphic("Cave_shop")
    self.Tprint('                                       ')
    self.Tprint('       You found a hidden Shop         ')
    self.Tprint('                                       ')
    self.Tprint('.......................................')
    self.Tprint('...............______..................')
    self.Tprint('............\ /       \ /..............')
    self.Tprint('........... /-         -\..............')
    self.Tprint('...........|    _        |.............')
    self.Tprint("...........|  {'^'}      |.............")
    self.Tprint('...........| ^-{ }-8   $_|.............')
    self.Tprint('...........|   ( )     _\|.............')
    self.Tprint('...........|__/___\___|__|.............')
    self.Tprint('.......................................')

    self.SetCurrentGraphic("Cave_tunnel")
    self.Tprint('                                       ')
    self.Tprint('       You found a new tunnel          ')
    self.Tprint('                                       ')
    self.Tprint('.......................................')
    self.Tprint('...............______..................')
    self.Tprint('............\ /       \ /..............')
    self.Tprint('........... /-         -\..............')
    self.Tprint('...........|             |.............')
    self.Tprint('...........|             |.............')
    self.Tprint('...........|             |.............')
    self.Tprint('...........|             |.............')
    self.Tprint('...........|_____________|.............')
    self.Tprint('.......................................')

    self.SetCurrentGraphic("Cave_Wall")
    self.Tprint('                                       ')
    self.Tprint('      You have ran into a wall         ')
    self.Tprint('                                       ')
    self.Tprint('..........._______________.............')
    self.Tprint('........\ /################\ /.........')
    self.Tprint('......../####################\.........')
    self.Tprint('........|####################|.........')
    self.Tprint('........|####################|.........')
    self.Tprint('........|####################|.........')
    self.Tprint('........|####################|.........')
    self.Tprint('........|####################|.........')
    self.Tprint('........|####################|.........')
    self.Tprint('.......................................')

    self.SetCurrentGraphic("King")
    self.Tprint(" ")
    self.Tprint("                      +                ")
    self.Tprint("                     vAv .-.           ")
    self.Tprint('                     (")| # |          ')
    self.Tprint("                    / v \\# | + o      ")
    self.Tprint("                   c\\  //=.-'O/\"-.   ")
    self.Tprint('                   |/~."|  |"-/.-\'|   ')
    self.Tprint("                   / .  (__|   |  |    ")
    self.Tprint("                  (=/===)`  ~-.|.-'    ")

    self.SetCurrentGraphic("Fin")
    self.Tprint(" ")
    self.Tprint("              _          _                          ")
    self.Tprint("             | |_ ___   | |__   ___                 ")
    self.Tprint("             | __/ _ \  | '_ \ / _ \                ")
    self.Tprint("             | || (_) | | |_) |  __/                ")
    self.Tprint("              \__\___/  |_.__/ \___|                ")
    self.Tprint("                  _   _                      _      ")
    self.Tprint("   ___ ___  _ __ | |_(_)_ __  _   _  ___  __| |     ")
    self.Tprint("  / __/ _ \| '_ \| __| | '_ \| | | |/ _ \/ _` |     ")
    self.Tprint(" | (_| (_) | | | | |_| | | | | |_| | __/ |(_| |     ")
    self.Tprint("  \___\___/|_| |_|\__|_|_| |_|\__,_|\___|\__,_|     ")

    self.SetCurrentGraphic("Castle")
    self.Tprint(" ")
    self.Tprint("                        _              ")
    self.Tprint("                       /^\             ")
    self.Tprint("                       | |             ")
    self.Tprint("                   _   |-|             ")
    self.Tprint("            _    _/^\_ | |             ")
    self.Tprint("           /^\  / [_] \+-+             ")
    self.Tprint("   _      |---||-------| |_       _    ")
    self.Tprint(" _/^\_    _/^\_|  [_]  |_/^\_   _/^\_  ")
    self.Tprint(" |!_!|    |!_!||_______||!_!|   |!_!|  ")
    self.Tprint("  | |======| |===========| |=====| |   ")
    self.Tprint("  |!|      | |    /^\    | |     |!|   ")
    self.Tprint("  | |      |!|   |   |   |!|     | |   ")
    self.Tprint("  |_|______|_|__ |   |___|_|_____|_|   ")

    self.SetCurrentGraphic("Logo")
    self.Tprint(" ")
    self.Tprint("                      ,     \    /      ,                     ")
    self.Tprint("                     / \    )\__/(     / \                    ")
    self.Tprint("                    /   \  (_\  /_)   /   \                   ")
    self.Tprint(" __________________/_____\__\@  @/___/_____\_________________ ")
    self.Tprint(" |            ____          |\../|        _                 | ")
    self.Tprint(" |           |  _ \          \VV/        (_)                | ")
    self.Tprint(" |           | |_) | __ ___   ____ _ _ __ _  __ _           | ")
    self.Tprint(" |           |  _ < / _` \ \ / / _` | '__| |/ _` |          | ")
    self.Tprint(" |           | |_) | (_| |\ V / (_| | |  | | (_| |          | ")
    self.Tprint(" |           |____/ \__,_| \_/ \__,_|_|  |_|\__,_|          | ")
    self.Tprint(" |__________________________________________________________| ")
    self.Tprint("             |    /\ /      \\       \ /\    |     a game     ")
    self.Tprint("             |  /   V        ))       V   \  |      from      ")
    self.Tprint("             |/     `       //        '     \|     MURKSEC    ")
    self.Tprint("             `              V                '                ")
    self.Tprint(" ")

    self.SetCurrentGraphic("Cave_fairy")
    self.Tprint('')
    self.Tprint(    'You have discovered a magical fairy')
    self.Tprint('')
    self.Tprint(''' **You drink from the fairy\'s fountain
        and feel refreshed**''')
    self.Tprint('.......................................')
    self.Tprint('...|               *              |....')
    self.Tprint('...|     *                        |....')
    self.Tprint('...|     ___    hey!              |....')
    self.Tprint('...| * ໒(ಠ_ಠ)७    listen!        |....')
    self.Tprint('...|     /-\    *                 |....')
    self.Tprint('...|                    _^|^_     |....')
    self.Tprint('...|  *  _____________ |_???_|    |....')
    self.Tprint('.......................................')

    self.SetCurrentGraphic("Cave_Door")
    self.Tprint('')
    self.Tprint('       You have found a door           ')
    self.Tprint('     ***The door is locked***          ')
    self.Tprint('.......................................')
    self.Tprint('............._________.................')
    self.Tprint('............|*********|................')
    self.Tprint('............|*********|................')
    self.Tprint('............|*********|................')
    self.Tprint('............|*******0*|................')
    self.Tprint('............|*********|................')
    self.Tprint('............|*********|................')
    self.Tprint('............|_________|................')
    self.Tprint('.......................................')

    self.SetCurrentGraphic("Boss_Door")
    self.Tprint('')
    self.Tprint('   You have found a creepy door        ')
    self.Tprint('     ***The door is locked***          ')
    self.Tprint('.......................................')
    self.Tprint('............._________.................')
    self.Tprint('............|         |................')
    self.Tprint('............|   ???   |................')
    self.Tprint('............|  ?___?  |................')
    self.Tprint('............|  / * \  |................')
    self.Tprint('............|  \_µ_/  |................')
    self.Tprint('............|         |................')
    self.Tprint('............|_________|................')
    self.Tprint('.......................................')

    self.SetCurrentGraphic("Boss_Door_Unlocked")
    self.Tprint('')
    self.Tprint('   You have found a creepy door        ')
    self.Tprint(' **You use the skull key to open it**  ')
    self.Tprint('.......................................')
    self.Tprint('............._________.................')
    self.Tprint('............|         |................')
    self.Tprint('............|   ???   |................')
    self.Tprint('............|  ?___?  |................')
    self.Tprint('............|  / * \  |................')
    self.Tprint('............|  \_µ_/  |................')
    self.Tprint('............|         |................')
    self.Tprint('............|_________|................')
    self.Tprint('.......................................')

    self.SetCurrentGraphic("Boss_Killed")
    self.Tprint('                                       ')
    self.Tprint('                                       ')
    self.Tprint('                                       ')
    self.Tprint('.......................................')
    self.Tprint('...............______..................')
    self.Tprint('............\ /       \ /..............')
    self.Tprint('........... /-         -\..............')
    self.Tprint('...........|    ______   |.............')
    self.Tprint('...........|   |      |  |.............')
    self.Tprint('...........|_  |  &&  | _|.............')
    self.Tprint('...........|@@\   __  /@@|.............')
    self.Tprint('...........|@@|__|__|_|@@|.............')
    self.Tprint('.......................................')

    self.SetCurrentGraphic("Cave_Door_Unlocked")
    self.Tprint('')
    self.Tprint('       You have found a door           ')
    self.Tprint('  ***You use your key to open it***    ')
    self.Tprint('.......................................')
    self.Tprint('............._________.................')
    self.Tprint('............|*********|................')
    self.Tprint('............|*********|................')
    self.Tprint('............|*********|................')
    self.Tprint('............|*******0*|................')
    self.Tprint('............|*********|................')
    self.Tprint('............|*********|................')
    self.Tprint('............|_________|................')
    self.Tprint('.......................................')

    self.SetCurrentGraphic("Cave_box")
    self.Tprint('')
    self.Tprint('    You have found a treasure chest    ')
    self.Tprint('                                       ')
    self.Tprint('..........___________________..........')
    self.Tprint('......../   ____.______.____  \........')
    self.Tprint(".......|   \`\           /'/   |.......")
    self.Tprint('.......|    >|___,___,___|<    |.......')
    self.Tprint('.......|    /d$$$P$,$__sss.\   |.......')
    self.Tprint('.......|   / $$$$$$$$$$$$$b \  |.......')
    self.Tprint('.......|  <=====w=====w=====>  |.......')
    self.Tprint('.......|   \ \____> <____/ /   |.......')
    self.Tprint('.......|    \_____________/    |.......')
    self.Tprint('........-----------------------........')

    self.SetCurrentGraphic("Goblin")
    self.Tprint('')
    self.Tprint('..........___________________..........')
    self.Tprint('......../                     \........')
    self.Tprint('.......|                       |.......')
    self.Tprint('.......|          ,_,          |.......')
    self.Tprint('.......|         (ʘ_ʘ)  W      |.......')
    self.Tprint('.......|      d--->|<---|      |.......')
    self.Tprint('.......|          |.|   |      |.......')
    self.Tprint('.......|          )-(          |.......')
    self.Tprint('.......|        _/   \_        |.......')
    self.Tprint('........-----------------------........')

    self.SetCurrentGraphic("Spider2")
    self.Tprint('')
    self.Tprint('.......................................')
    self.Tprint('.......................................')
    self.Tprint('.......-------------------------.......')
    self.Tprint('...../                           \.....')
    self.Tprint('....|                             |....')
    self.Tprint('....|                             |....')
    self.Tprint('....|        _ _ _ _ _ _ _        |....')
    self.Tprint('....| ミ /╲/( ͜。 ͜。 ͡ʖ ͜。 ͜。)/\╱\   |....')
    self.Tprint('....|   / /\              / /\ \  |....')
    self.Tprint('....|_____________________________|....')
    self.Tprint('.......................................')

    self.SetCurrentGraphic("Spider")
    self.Tprint('')
    self.Tprint('.......................................')
    self.Tprint(".......___________________________......")
    self.Tprint("...../._:_:__:_:_:__:____:_ _ _\\.\.....")
    self.Tprint("....| :\`.;-._: : :  :_,-/  .  \ \'|....")
    self.Tprint("....| `_\'`. '`-._:.-' \ \_(。v)_/ |....")
    self.Tprint("....|  ;_\ ,`./  /      >==/|\==<  |....")
    self.Tprint("....|.`   \ ,'`./        /(-+-)\\  |....")
    self.Tprint("....|_ `',~\  .'         \ \|/ /|  |....")
    self.Tprint("....|   `_.-\'                     |....")
    self.Tprint("....|______________________________|....")
    self.Tprint("...................................|....")

    self.SetCurrentGraphic("Boss")
    self.Tprint('')
    self.Tprint('........._____________________.........')
    self.Tprint('......./          ,w,          \.......')
    self.Tprint('......|          (ʘ,ʘ)   {#}    |......')
    self.Tprint('......|           \@/     |     |......')
    self.Tprint('......|     d===>(.I.)<===|     |......')
    self.Tprint('......|          ( . )    |     |......')
    self.Tprint('......|           /#\     |     |......')
    self.Tprint('......|          // \\\    |     |......')
    self.Tprint('......|        _//   \\\_        |......')
    self.Tprint('.......-------------------------.......')

    self.SetCurrentGraphic("Class Selection")
    self.Tprint("")
    self.Tprint(" `,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,` ")
    self.Tprint(" `,`                                      _+       |   `,` ")
    self.Tprint(" `,`                 /`------------------' |  \+/  |   `,` ")
    self.Tprint(" `,`                 \_|CHOOSE YOUR CLASS|_| _<=>_ |   `,` ")
    self.Tprint(" `,`  1 = Fighter      `-----------------' 0/ \ / o=o  `,` ")
    self.Tprint(" `,`  2 = Monk                             \/\ ^ /`0   `,` ")
    self.Tprint(" `,`  3 = Thief                            | /_^_\     `,` ")
    self.Tprint(" `,`  4 = Mage                             | || ||     `,` ")
    self.Tprint(" `,`                          _____________|_d|_|b____ `,` ")
    self.Tprint(" `,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,` ")

    self.SetCurrentGraphic("Cottage")
    self.Tprint("")
    self.Tprint("                            ~~~~              ")
    self.Tprint("                           ~~                 ")
    self.Tprint("                         _||____              ")
    self.Tprint("   /\ /\ /\             /\\\\\\\\             ")
    self.Tprint("  //\\/\\/\\           /__\\\\\\\\  _,        ")
    self.Tprint("  //\\/\\/\\           |__|_|_|__|   \__,     ")
    self.Tprint("   || || ||            |  |/|\| /|   /\ \     ")
    self.Tprint("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   ")

    self.SetCurrentGraphic("Mountain Castle")
    self.Tprint("")
    self.Tprint("          /\                                                     ")
    self.Tprint("         /**\                                                    ")
    self.Tprint("        /****\   /\                                              ")
    self.Tprint("       /      \ /**\                                             ")
    self.Tprint("      /  /\    /    \        /\    /\    _   |~  _         /\/\/ ")
    self.Tprint("     /  /  \  /      \      /  \/\/  \  [_]--'--[_]   /\  /\/ /  ")
    self.Tprint("    /  /    \/ /\     \    /    \ \     |'|""`""|'|  /  \/  \    ")
    self.Tprint("   /  /      \/  \/\   \  /      \      | | /^\ | |              ")
    self.Tprint("__/__/_______/___/__\___\_______________|_|_|I|_|_|______________")


    self.SetCurrentGraphic("Death One")
    self.Tprint(' ')
    self.Tprint('__  ______  __  __       ____  ______________  ')
    self.Tprint('\ \/ / __ \/ / / /      / __ \/  _/ ____/ __ \ ')
    self.Tprint(' \  / / / / / / /      / / / // // __/ / / / / ')
    self.Tprint(' / / /_/ / /_/ /      / /_/ // // /___/ /_/ /  ')
    self.Tprint('/_/\____/\____/      /_____/___/_____/_____/   ')

    self.SetCurrentGraphic("Death Two")
    self.Tprint(' ')
    self.Tprint('     )   )          (    (      (       ')
    self.Tprint('  ( /(( /(          )\ ) )\ )   )\ )    ')
    self.Tprint('  )\())\())    (   (()/((()/(( (()/(    ')
    self.Tprint(' ((_)((_)\     )\   /(_))/(_))\ /(_))   ')
    self.Tprint('__ ((_)((_) _ ((_) (_))_(_))((_|_))_    ')
    self.Tprint('\ \ / / _ \| | | |  |   \_ _| __|   \   ')
    self.Tprint(' \ V / (_) | |_| |  | |) | || _|| |) |  ')
    self.Tprint('  |_| \___/ \___/   |___/___|___|___/   ')

    self.SetCurrentGraphic("Death Three")
    self.Tprint(' ')
    self.Tprint("    ____  ____   ___   _____  _____   ") 
    self.Tprint("   |_  _||_  _|.'   `.|_   _||_   _|  ")
    self.Tprint("     \ \  / / /  .-.  \ | |    | |    ") 
    self.Tprint("      \ \/ /  | |   | | | '    ' |    ")
    self.Tprint("      _|  |_  \  `-'  /  \ \__/ /     ")
    self.Tprint("     |______|  `.___.'    `.__.'      ")
    self.Tprint(' ')
    self.Tprint("  ______   _____  ________  ______    ")
    self.Tprint(" |_   _ `.|_   _||_   __  ||_   _ `.  ")
    self.Tprint("   | | `. \ | |    | |_ \_|  | | `. \ ")
    self.Tprint("   | |  | | | |    |  _| _   | |  | | ")
    self.Tprint("  _| |_.' /_| |_  _| |__/ | _| |_.' / ")
    self.Tprint(" |______.'|_____||________||______.'  ")

    self.SetCurrentGraphic("Death Four")
    self.Tprint(' ')
    self.Tprint(" __   _______ _   _   ______ _____ ___________           __  ")
    self.Tprint(" \ \ / /  _  | | | |  |  _  \_   _|  ___|  _  \     _   / /  ")
    self.Tprint("  \ V /| | | | | | |  | | | | | | | |__ | | | |    (_) | |   ")
    self.Tprint("   \ / | | | | | | |  | | | | | | |  __|| | | |        | |   ")
    self.Tprint("   | | \ \_/ / |_| |  | |/ / _| |_| |___| |/ /      _  | |   ")
    self.Tprint("   \_/  \___/ \___/   |___/  \___/\____/|___/      (_) | |   ")
    self.Tprint("                                                        \_\  ")

    self.SetCurrentGraphic("Death Five")
    self.Tprint(' ')
    self.Tprint("   __   __      ______   _______  ______             _  _  ")
    self.Tprint("  |  | |  |    |      | |       ||      |      ___ (~ )( ~)")
    self.Tprint("  |  | |  |    |  _    ||    ___||  _    |    /   \_\ \/ / ")
    self.Tprint("  |  |_|  |    | | |   ||   |___ | | |   |   |   D_ ]\ \/  ")
    self.Tprint("  |       |    | |_|   ||    ___|| |_|   |   |   D _]/\ \  ")
    self.Tprint("  |       |    |       ||   |___ |       |    \___/ / /\ \ ")
    self.Tprint("  |_______|    |______| |_______||______|          (_ )( _)")

    self.SetCurrentGraphic("Death Six")
    self.Tprint(' ')
    self.Tprint("   _____         _____   ____   ____         _____   ")
    self.Tprint("  /     \       | ___ \ |_  _| | ___ \      /     \  ")
    self.Tprint(" | () () |      | |_/ /  | |   | |_/ /     | () () | ")
    self.Tprint("  \  ^  /       |    /   | |   |  __/       \  ^  /  ")
    self.Tprint("   |||||        | |\ \  _| |_  | |           |||||   ")
    self.Tprint("   |||||        \_| \_| \___/  \_|           |||||   ")

    self.SetCurrentGraphic("Death Seven")
    self.Tprint(' ')
    self.Tprint("      ,-=-.                  _       ")
    self.Tprint("     /  +  \               _| |_     ")
    self.Tprint("     |R.I.P|              |_   _|    ")
    self.Tprint("     | ~~~ |                | |      ")
    self.Tprint("\vV,,|_____|V,//vv,V,,/VvV,v|_|/,,   ")

    self.SetCurrentGraphic("Origin")
    self.Tprint(' ')
    self.Tprint("       ____________________________       ")
    self.Tprint("     / \                            \.    ")
    self.Tprint("    |  |                            |.    ")
    self.Tprint("     \_|         The Story          |.    ")
    self.Tprint("       |            of              |.    ")
    self.Tprint("       |                            |.    ")
    self.Tprint(f"       |            {Calradia.player.pname}            |.    ")
    self.Tprint("       |                            |.    ")
    self.Tprint("       |                            |.    ")
    self.Tprint("       |   _________________________|___  ")
    self.Tprint("       |  /                            /. ")
    self.Tprint("       \_/____________________________/.  ")

    self.SetCurrentGraphic("Wolf")
    self.Tprint('')
    self.Tprint("                     /\ /\\        /.\ ")
    self.Tprint("  /\                //\\\/\\  /\   // \\ ")
    self.Tprint(" //\\\               //\\\||  //\\\  // \\ ")
    self.Tprint(" //\\\     |\_/|      ||    ///\\\  | |")
    self.Tprint("  ||     / . .\            ///\\\     ")
    self.Tprint("         /( o )\          ////\\\\    ")
    self.Tprint("         / \ww\           //|/\|\\    ")
    self.Tprint("         | | | |            |  |      ")
    self.Tprint("       (~\ | | /~)          |  |      ")
    self.Tprint("     _/_\_|| ||_/_\_                  ")
    self.Tprint(" ___///_//_| |_\\__\\\______          ")

    self.SetCurrentGraphic("Dwarf")
    self.Tprint('')
    self.Tprint('.........                  ......')
    self.Tprint('......     ___    /\_--_/\  .....')
    self.Tprint('....      /___\   ||_||_||   ....')
    self.Tprint('...      (|0,0|)  \/ || \/   ....')
    self.Tprint('..     __ -{~}- __ -_P|      ....')
    self.Tprint('..    | /\  ~  /__/  []     .....')
    self.Tprint('...   |_| (____)     ||    ......')
    self.Tprint('....  \_]/______\    ||   .......')
    self.Tprint('.....    _\_||_/_    ||  ........')
    self.Tprint('......  (_,_||_,_)   || .........')

    self.SetCurrentGraphic("Fighter")
    self.Tprint('......    ___      /\     .....')
    self.Tprint('....     /###\     ||      ....')
    self.Tprint('...     (|0,0|)   o==o     ....')
    self.Tprint('..     __ \-/  _ -_@]      ....')
    self.Tprint('..    |/\  X  /_/         .....')
    self.Tprint('...   || |___|           ......')
    self.Tprint('....  \] /___\          .......')
    self.Tprint('....     | | |          .......')
    self.Tprint('.....    \_|_/         ........')
    self.Tprint('......  (,_|_,)       .........')

    self.SetCurrentGraphic("Thief")
    self.Tprint('......                   .....')
    self.Tprint('....     #####     |      ....')
    self.Tprint('...     (|0,0|)    |      ....')
    self.Tprint('..     __ \-/  __ o=o     ....')
    self.Tprint('..    |/\  v  /--\@I     .....')
    self.Tprint('...   || |___|          ......')
    self.Tprint('....  \] /___\         .......')
    self.Tprint('....     | | |         .......')
    self.Tprint('.....    \_|_/        ........')
    self.Tprint('......  (,_|_,)      .........')

    self.SetCurrentGraphic("Monk")
    self.Tprint('......                   .....')
    self.Tprint('....       .....          ....')
    self.Tprint('...       (|0,0|)         ....')
    self.Tprint('..       __| - |__        ....')
    self.Tprint('..      |/\ .I. /\|      .....')
    self.Tprint('...     || |_#_| ||     ......')
    self.Tprint('....    {] /___\ [}    .......')
    self.Tprint('....       | | |       .......')
    self.Tprint('.....      \_|_/      ........')
    self.Tprint('......    (,_|_,)    .........')

    self.SetCurrentGraphic("Mage")
    self.Tprint('......    / \     __     .....')
    self.Tprint('....     /___\   (())     ....')
    self.Tprint('...     (|0,0|)   ||      ....')
    self.Tprint('..      _ \-/  __ ||      ....')
    self.Tprint('..     |/| : |/--\@|     .....')
    self.Tprint('...    ||( : )    ||    ......')
    self.Tprint('....   \]|___|    ||   .......')
    self.Tprint('....     | | |    ||   .......')
    self.Tprint('.....    \_|_/    ||  ........')
    self.Tprint('......  (,_|_,)   || .........')
