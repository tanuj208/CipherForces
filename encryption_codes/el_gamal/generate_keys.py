from helper import *

def gen_keys():
	q = random.randint(pow(10, 20), pow(10, 50))
	g = random.randint(2, q)
	a = rand_coprime_with(q)
	h = power(g, a, q)

	public_key = [h,q,g]
	private_key = [a]
	return [public_key,private_key]

if __name__ == '__main__':
	a = gen_keys()
	print(a)