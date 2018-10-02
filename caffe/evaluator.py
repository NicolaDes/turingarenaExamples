import random

from turingarena import *

def create_random_instance(n):
    N = random.randint(2, n)
    A = [
        random.randint(0, N-1)
        for _ in range(0, N)
    ]
    B = [
        random.randint(A[_], N)
        for _ in range(0, N)
    ]
    return [N,A,B]

def run(algorithm, N, A, B):
    with run_algorithm(algorithm) as process:
        ret =  process.functions.pausa(N, A, B)
    print(f"Time usage: {process.time_usage}")
    return ret

def get_opt_cpp(N, A, B):
    correct_algo = os.environ["PWD"]+"/solutions/correct.cpp"
    return run(correct_algo,N,A,B)

def get_opt(N, A, B):
    T = [None]*2*N
    for i in range(0, N):
        T[i] = 2*A[i]+1
    for i in range(0, N):
        T[N+i] = 2*B[i]
    T.sort()
    for i in range(0, 2*N):
        T[i] %= 2
    c = 0
    caffe = 0
    for i in range(0, 2*N):
        if T[i] == 1:
            c = c+1
            caffe += c
        else:
            c = c-1
    return caffe


def main():
    algorithm = submission.source
    goals = {
        "exponential": True,
        "quadratic": True,
        "n_log_n": True,
    }

    for gs, ns in [
        (["exponential", "quadratic", "n_log_n"], [100] * 3),
        (["quadratic", "n_log_n"], [1000]),
        (["n_log_n"], [10000]),
    ]:
        for n in ns:
            if not any(goals[g] for g in gs):
                break

            print(f"Testing n={n}")
            [N,A,B] = create_random_instance(n)
            opt = get_opt_cpp(N,A,B)
            try:
                submitted = run(algorithm, N,A,B)
            except AlgorithmError as e:
                print("Error:", e)
                correct = False
            else:
                print("Your solution:", submitted)
                print("Optimal solution:", opt)
                correct = (
                    opt==submitted
                )
                print("Correct:", correct)
            if not correct:
                for g in gs:
                    goals[g] = False
            print("------------------")
    evaluation.data(dict(goals=goals))

if __name__ == "__main__":
    main()
