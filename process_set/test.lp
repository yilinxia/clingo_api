
% Maximum number of states ("emergency brake")
#const n = 12.

e(a,b). e(b,c). e(c,d). e(d,e). e(e,f). e(f,a).

fr. % use frame rule, otherwise termination check fails 
% dr. % use double-recursive rule
rr. % use right-recursive rule
 
% Initialize transitive closure tc/2 from facts e/2:
tc(0, X,Y) :- e(X,Y).

% Frame rule: keep everything you had
tc(N1, X,Y) :- fr, next(N,N1),
	       tc(N, X,Y).

% % (dr) variant: double-recursive rule
% tc(N1, X,Y) :- dr, next(N,N1),
% 	       tc(N, X,Z),
% 	       tc(N, Z,Y).

% (rr) variant: right-recursive rule
tc(N1, X,Y) :- rr, next(N,N1),
	       e(X,Z),
	       tc(N, Z,Y).

% Which atoms have been newly derived in this round? 
new_tc(N1,X,Y) :- next(N,N1),
	       tc(N1,X,Y),
	       not tc(N,X,Y).

% Compute next state, if there's a need for it
next(0,1). 
next(N1,N2) :- next(N,N1), N2 = N1+1,
	       new_tc(N1, _, _), % if there's something new in N1 => create N2
	       N1 < n.        % this emergency brake is necessary (unfair eval/grounding strategy)

% What's the max state index used? 
max_state(N1) :- next(N,N1), not next(N1, N1+1).

%#show tc/3.
#show new_tc/3.
#show max_state/1.
