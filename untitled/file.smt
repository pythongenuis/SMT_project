(set - logic ALL)
(set - option :produce-models true)
(assert ( (and (not ( p1 and p2 and p3)( p1 and p2 and p3))(p1 and p2 and (not  p3) ))))
(check - sat)