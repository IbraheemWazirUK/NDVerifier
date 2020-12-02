# NDVerifier

## Running the program
suppose your ND proof is in <proof_file>
In terminal run:
```
$ python3 main.py <proof_file>
```

## given and ass
the given keyword supposes the expression to be true
```
given <expression>;
```
the ass keyword assumes the expression is true in a new block
mainly used for implications and contradictions
```
	ass p;
	...
	q;
p -> q;

	ass A;
	...
	false;
not A;
```

## And Elimination
if (p and q) is somehow derived, then p is true and q is true
```
given p and q;

p;
q;
```

## And Introduction
if p is somehow proven and q is somehow proven, then (p and q) is true
```
given p;
given q;

p and q;
```

## Or Elimination
if (p or q) is somehow proven, and p -> r is proven and q -> r is proven, then r is true
```
given p or q;
given p -> r;
given q -> r;

r;
```

## Or Introduction
if p is somehow proven or q is somehow proven, then (p or q) is true
```
given p;
p or q;
```

```
given q;
p or q;
```

## Not Elimination
if not not p is some how proven, then p is true
```
given not not p;
p;
```
if p is somehow proven and not p is proven then false is derived
```
given p;
given not p;

false;
```

## Not Introduction
if p is assumed and false is derived in the block, then not p is true
```
	ass p;
	...
	false;

not p;
```

## -> Elimination
if p is somehow proven and p -> q is proven then q is true

```
given p;
given p -> q;

q;
```

## -> Introduction
if p is assumed and q is derived in the same block, then p -> q is true
```
	ass p;
	...
	q;

p -> q;
```

## <-> Elimination

if p is somehow proven and p <-> q is proven then q is true
```
given p;
given p <-> q;

q;
```

if q is somehow proven and p <-> q is proven then p is true
```
given q;
given p <-> q;

p;
```
## <-> Introduction
if p -> q is somehow proven and q -> p is somehow proven, then p <-> q is true;
```
given p -> q;
given q -> p;

p <->q;
```

## False Elimination
any expression can be derived from false (since false -> A is true for all A)
```
given false;

p; 
```
## False Introduction
Same as not elimination
```
given not p;
given p;
false;
```