
from methods import matching


def test_basic():

    in_ = '([])({})'
    assert matching.iscorrect(in_)
    assert not matching.iscorrect(in_ + '(')


def test_fixer():
    in_ = '([)({})'
    assert matching.iscorrect(matching.fix_matchs(in_))


#/BracesMatch/enigma1
#{()(){[[]{}]}}[]()<>[]<{[]}(<()>)><<[]>[({{}})

#
#/BracesMatch/answer1
#}]}]]]}]}]})>)>)>>}]]})}]>)>}>)>}])>)))))})>
##
#/BracesMatch/enigma2
##	$
#{<>{}}<[<[(())[([()])[]{{}()}]]>[(){}[]]]
#/BracesMatch/answer2
#]])})>}}>)))]>
#
#
#/BracesMatch/enigma3
#(<()>(<[][]>)<>[[(()())]]())<>[]{}[][]<>{}<

#/BracesMatch/answer3
#)})]))]}]}]}))}])]}>
#
#/BracesMatch/enigma4
#<>[<{[]}>[{{{{{}}}<>}(<()>()[<{{}}{[{<<>[[

#/BracesMatch/answer4
#))]}])}]>>>>)]]]>>]}})>}>}))))>]}>]]
#
#/BracesMatch/enigma5
#[[]<>{<>}<>][()<>]<{}>{{<[([])[()]][]>({})

#/BracesMatch/answer5
#])]]>})}}>>)])]]]}>>}}))>]>])}]]]]))
#
#/BracesMatch/enigma6
#[]{}[{<>}[{<()><[]>}][]]{(<>)}({})()[]<[[

#/BracesMatch/answer6
#}>>>>})))))>]]}>>]]>>)})}})>})>)])
#
#/BracesMatch/enigma7
#<>{}{}[({}[{(<><{}(<<>>){[[]]}[](<>([]
#
#/BracesMatch/answer7
#}}>>>})})})}>)]>}]}]]))}}}]])>}]>]]])}]>)}>]])
#

#/BracesMatch/enigma8
#()[][](<>){}(<>)([])()<>({}()(([]{})<>)

#/BracesMatch/answer8
#]>>}})}]}]))}]>)]]>]}])}>]
#
#/BracesMatch/enigma9
#{()}<()[]<<>>[]>[]<>[((){}){}]({()}){{<({[[]]})

#/BracesMatch/answer9
#}]>])}>]>}])}]})>>>]>)]}>>)]
