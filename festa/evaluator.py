import festa.instances
import festa.solver

from turingarena import *


def run(algorithm, N, M, conoscenzeA, conoscenzeB):
    with run_algorithm(submission.source) as process:
        ret = process.functions.invita(N, M, conoscenzeA, conoscenzeB)
    return [process.time_usage, ret]


def main():
    algorithm = submission.source
    goals = {
        "exponential": True,
        "quadratic": True,
        "linear": True,
    }

    for gs, ns in [
        (["exponential", "quadratic", "linear"], [10] * 3),
        (["quadratic", "linear"], [1000] * 2),
        (["linear"], [10000]),
    ]:
        print(f"Testing {gs[0]}\n")
        for n in ns:
            if not any(goals[g] for g in gs):
                break

            [N, M, conoscenzeA,
                conoscenzeB] = festa.instances.create_random_instance(n)
            opt = festa.solver.solve(N, M, conoscenzeA, conoscenzeB)
            try:
                [time_usage, submitted] = run(
                    algorithm, N, M, conoscenzeA, conoscenzeB)
            except AlgorithmError as e:
                print("Error:", e)
                correct = False
            else:
                print(f"Correct: {opt==submitted}, time usage: {format(time_usage,'.12g')}")
                correct = (
                    opt == submitted and
                    time_usage <= festa.max_time
                )
            if not correct:
                for g in gs:
                    goals[g] = False
        print("------------------")
    evaluation.data(dict(goals=goals))


if __name__ == "__main__":
    main()
