# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-20 17:53:02
# @LastEditors: llseng
# @LastEditTime: 2021-01-20 17:53:03
#

import abc, random

class Warrior(object, metaclass = abc.ABCMeta):
    """
    战士
    """

    __slots__ = ( '_name', '_hp' )

    @staticmethod
    def is_valid( W ):
        if W.hp <= 0:
            return True
        return False

    def __init__( self, name, hp ):
        self.name = name
        self._hp = hp
    
    @property
    def name( self ):
        return self._name

    @name.setter
    def name( self, name ):
        self._name = name
    
    @property
    def hp( self ):
        return self._hp
    
    @hp.setter
    def hp( self, hp ):
        # 防御
        if self.hp > hp:
            if self.hp - hp < self.defense():
                hp = self.hp
            else:
                hp += self.defense()
            print( "%s 受到实际伤害 %d" % (self.name, self.hp - hp) )
        
        self._hp = hp
            
    
    @abc.abstractmethod
    def attack( self, other ):
        pass

    @abc.abstractmethod
    def defense( self ):
        pass

    def __str__( self ):
        return "%s: hp %d" % (self.name, self.hp)

    def __repr__( self ):
        return self.__str__()

class Taoist( Warrior ):
    """
    道士
    """
    __slots__ = ('_name', '_hp', '_mp', '_attack_num')

    def __init__( self, name, hp, mp = 100 ):
        super().__init__( name, hp )
        self.mp = mp
        self._attack_num = 0

    @property
    def mp( self ):
        return self._mp
    
    @mp.setter
    def mp( self, mp ):
        self._mp = mp
    
    def attack( self, other ):
        self._attack_num += 1
        hurt = 0
        if random.randint(1, 10) > 2:
            hurt = 10
        else:
            hurt = self.mp

        print( "%s 攻击 %s 造成 %d 伤害" % (self.name, other.name, hurt) )
        other.hp -= hurt
    
    def defense( self ):
        return 2

class Soldier( Warrior ):
    """
    力士
    """
    __slots__ = ('_name', '_hp', '_sp')

    def __init__( self, name, hp, sp = 100 ):
        super().__init__( name, hp )
        self.sp = sp
    
    @property
    def sp( self ):
        return self._sp

    @sp.setter
    def sp( self, sp ):
        self._sp = sp

    def attack( self, other ):
        hurt = self.sp // 10 + 10

        print( "%s 攻击 %s 造成 %d 伤害" % (self.name, other.name, hurt) )
        other.hp -= hurt

    def defense( self ):
        return 4

if __name__ == "__main__":
    T = Taoist( '林寒潮', 1000, 150 )
    Ss = []
    Ss.append( Soldier( '武大', 700, 30 ) )
    Ss.append( Soldier( '刘二', 400, 110 ) )
    Ss.append( Soldier( '张三', 600, 90 ) )
    Ss.append( Soldier( '李四', 200, 200 ) )

    def show_s():
        print( T )
        for x in Ss:
            print( x, end='; ' )
        print()
    
    show_s()

    ss = Ss.copy()
    while len( ss ):
        if Warrior.is_valid( T ):
            break
        for s in ss:
            if Warrior.is_valid( T ):
                break
            T.attack( s )
            if Warrior.is_valid( s ):
                ss.remove( s )
            else:
                s.attack( T )
        
        show_s()
    
    print( "exit" )
    show_s()