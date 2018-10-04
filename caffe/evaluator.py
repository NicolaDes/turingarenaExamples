import caffe.instances
import caffe.solver

from turingarena import *


def run(algorithm, N, A, B):
    with run_algorithm(algorithm) as process:
        ret =  process.functions.pausa(N, A, B)
    print(f"Time usage: {process.time_usage}")
    return [process.time_usage,ret]


def main():
    algorithm = submission.source
    goals = {
        "exponential": True,
        "quadratic": True,
        "linear": True,
    }

    for gs, ns in [
        (["exponential"], [10] * 3 ),
        (["quadratic"], [1000] * 2),
        (["linear"], [4000]),
    ]:
        print(f"Verifying {gs[0]}\n")
        for n in ns:
            if not any(goals[g] for g in gs):
                break

            # Get instance of the problem
            [N,A,B] = caffe.instances.create_random_instance(n)

            # Get optimal solution from [package]
            opt = caffe.solver.solve(N,A,B)
            try:
                # Compute submitted algorithm
                [time_usage,submitted] = run(algorithm, N,A,B)
            except AlgorithmError as e:
                # Also time more than 1s is taken here (turingarena launch an exception)
                print("Error:", e)
                correct = False
            else:
                print(f"Correct: {opt==submitted}, time usage: {time_usage}")
                # Correct if solution is the same and time is under the limit
                correct = (
                    opt==submitted and
                    time_usage <= caffe.max_time
                )
            if not correct:
                for g in gs:
                    goals[g] = False
        print("------------------")
    evaluation.data(dict(goals=goals))

if __name__ == "__main__":
    main()
