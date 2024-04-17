import numpy as np

__all__ = ['bound', 'benchmark_result', 'terminate']


def bound(a, upper_bound, lower_bound):
    """
    Enforce upper and lower bounds on an array.

    Args:
        a (np.array): The array to apply bounds to.
        upper_bound (float or np.array): Upper boundary for array elements.
        lower_bound (float or np.array): Lower boundary for array elements.

    Returns:
        np.array: The bounded array, with all elements clipped to the
        specified bounds.
    """
    a[a > upper_bound] = upper_bound[a > upper_bound]
    a[a < lower_bound] = lower_bound[a < lower_bound]
    return a


def benchmark_result(x, benchmark_number):
    """
    Calculate the result of a benchmark function specified by the
    benchmark number.

    Args:
        x (np.array): An array of input values for which the benchmark
        function is evaluated.
        benchmark_number (int): The identifier of the benchmark function
        to use.

    Returns:
        float: The result of the benchmark function computation.
    """
    if benchmark_number == 1:
        y = (
            (1.5 - x[0] + x[0] * x[1])**2 +
            (2.25 - x[0] + x[0] * x[1]**2)**2 +
            (2.625 - x[0] + x[0] * x[1]**3)**2
        )

    elif benchmark_number == 2:
        y = -np.cos(x[0]) * np.cos(x[1]) * \
            np.exp(-((x[0] - np.pi)**2 + (x[1] - np.pi)**2))

    elif benchmark_number == 3:
        y = 0.26 * (x[0]**2 + x[1]**2) - 0.48 * x[0] * x[1]

    elif benchmark_number == 4:
        y = (
            x[0]**2 + 2 * x[1]**2
            - 0.3 * np.cos(3 * np.pi * x[0])
            - 0.4 * np.cos(4 * np.pi * x[1])
            + 0.7
        )

    elif benchmark_number == 5:
        y = (x[0]**2 * x[1] - 7)**2 + (2 * x[0] + x[1] - 5)**2

    elif benchmark_number == 6:
        m = 10
        d = len(x)
        sum = 0
        for i in range(d):
            xi = x[i]
            new_term = np.sin(xi) * np.sin((i + 1) * xi**2 / np.pi)**(2 * m)
            sum += new_term
        y = -sum

    elif benchmark_number == 7:
        radius_squared = x[0]**2 + x[1]**2
        sin_term = np.sin(np.sqrt(radius_squared))**2
        denominator = 1 + 0.001 * radius_squared**2
        y = 0.5 + (sin_term - 0.5) / denominator

    elif benchmark_number == 8:
        term1 = 4 * x[0]**2
        term2 = -2.1 * x[0]**4
        term3 = (1/3) * x[0]**6
        term4 = x[0] * x[1]
        term5 = -4 * x[1]**2
        term6 = 4 * x[1]**4
        y = term1 + term2 + term3 + term4 + term5 + term6

    elif benchmark_number == 9:
        cosine_arg = (3 * np.pi * x[0]) * (4 * np.pi * x[1])
        cosine_term = -0.3 * np.cos(cosine_arg)
        y = x[0]**2 + 2 * x[1]**2 + cosine_term + 0.3

    elif benchmark_number == 10:
        cosine_arg = (3 * np.pi * x[0]) + (4 * np.pi * x[1])
        cosine_term = -0.3 * np.cos(cosine_arg)
        y = x[0]**2 + 2 * x[1]**2 + cosine_term + 0.3

    elif benchmark_number == 11:
        sum1 = 0
        sum2 = 0
        for i in range(1, 6):
            sum1 += i * np.cos((i + 1) * x[0] + i)
            sum2 += i * np.cos((i + 1) * x[1] + i)
        y = sum1 * sum2

    elif benchmark_number == 12:
        term1 = 100 * (x[0]**2 - x[1])**2
        term2 = (x[0] - 1)**2
        term3 = (x[2] - 1)**2
        term4 = 90 * (x[2]**2 - x[3])**2
        term5 = 10.1 * ((x[1] - 1)**2 + (x[3] - 1)**2)
        term6 = 19.8 * (x[1] - 1) * (x[3] - 1)
        y = term1 + term2 + term3 + term4 + term5 + term6

    elif benchmark_number == 13:
        m = 10
        d = len(x)
        sum = 0
        for i in range(d):
            xi = x[i]
            new_term = np.sin(xi) * np.sin((i + 1) * xi**2 / np.pi)**(2 * m)
            sum += new_term
        y = -sum

    elif benchmark_number == 14:
        n = len(x)
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for i in range(n):
            sum1 += x[i]**2
            sum2 += 0.5 * i * x[i]
            sum3 += 0.5 * i * x[i]
        y = sum1 + (sum2)**2 + (sum3)**4

    elif benchmark_number == 15:
        m = 10
        d = len(x)
        sum = 0
        for i in range(d):
            xi = x[i]
            new_term = np.sin(xi) * np.sin((i + 1) * xi**2 / np.pi)**(2 * m)
            sum += new_term
        y = -sum

    elif benchmark_number == 16:
        n = len(x)
        sum1 = 0
        for i in range(n):
            sum1 += (x[i] + 0.5)**2
        y = sum1

    elif benchmark_number == 17:
        y = np.sum(np.array(x)**2)

    elif benchmark_number == 18:
        n = len(x)
        sum1 = 0
        for i in range(n):
            sum1 += i * x[i]**2
        y = sum1

    elif benchmark_number == 19:
        n = len(x)
        sum1 = 0
        for i in range(n):
            sum1 += i * x[i]**4
        y = sum1 + np.random.rand()

    elif benchmark_number == 20:
        n = len(x)
        sum1 = 0
        sum2 = 1
        for i in range(n):
            sum1 += (x[i]**2)**0.5
            sum2 *= (x[i]**2)**0.5
        y = sum1 + sum2

    elif benchmark_number == 21:
        n = len(x)
        sum1 = 0
        for i in range(n):
            for j in range(1, i + 1):
                sum1 += x[j]**2
        y = sum1

    elif benchmark_number == 22:
        n = len(x)
        y = 0
        for i in range(n - 1):
            y += 100 * (x[i + 1] - x[i]**2)**2 + (x[i] - 1)**2

    elif benchmark_number == 23:
        n = len(x)
        sum1 = (x[0] - 1)**2
        sum2 = 0
        for i in range(1, n):
            sum2 += i * (2 * x[i]**2 - x[i - 1])**2
        y = sum1 + sum2

    elif benchmark_number == 24:
        n = len(x)
        s = 0
        for j in range(n):
            s += (x[j]**2 - 10 * np.cos(2 * np.pi * x[j]))
        y = 10 * n + s

    elif benchmark_number == 25:
        n = len(x)
        fr = 4000
        s = 0
        p = 1
        for j in range(n):
            s += x[j]**2
        for j in range(n):
            p *= np.cos(x[j] / np.sqrt(j + 1))
        y = s / fr - p + 1

    elif benchmark_number == 26:
        n = len(x)
        a = 20
        b = 0.2
        c = 2 * np.pi
        s1 = 0
        s2 = 0
        for i in range(n):
            s1 += x[i]**2
            s2 += np.cos(c * x[i])
        y = -a * np.exp(-b * np.sqrt(1 / n * s1)) \
            - np.exp(1 / n * s2) + a + np.exp(1)
    return y


def terminate(benchmark_number):
    """
    Determine the termination criteria for a given benchmark scenario.

    Args:
        benchmark_number (int): The identifier of the benchmark function
        for which to define termination criteria.

    Returns:
        tuple: A tuple containing global minimum, lower bounds,
        upper bounds, dimensionality of the benchmark (nd), and
        the maximum number of allowed iterations (max_limit).
    """
    max_limit = 500000  # maximum number of function evaluations
    Tol = 1e-5  # default is 1e-5

    if benchmark_number == 1:
        Lb = -4.5
        Ub = 4.5
        nd = 2  # number of variables
        Lb = np.ones(nd) * Lb  # upper bound
        Ub = np.ones(nd) * Ub  # lower bound
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 2:
        Lb = -100
        Ub = 100
        nd = 2
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = -1
        globalMin += Tol
    elif benchmark_number == 3:
        Lb = -10
        Ub = 10
        nd = 2
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 4:
        Lb = -100
        Ub = 100
        nd = 2
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 5:
        Lb = -10
        Ub = 10
        nd = 2
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 6:
        Lb = 0
        Ub = np.pi
        nd = 2
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = -1.8013
        globalMin += Tol
    elif benchmark_number == 7:
        Lb = -100
        Ub = 100
        nd = 2
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 8:
        Lb = -5
        Ub = 5
        nd = 2
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = -1.0316284534898
        globalMin += Tol
    elif benchmark_number == 9:
        Lb = -100
        Ub = 100
        nd = 2
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 10:
        Lb = -100
        Ub = 100
        nd = 2
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 11:
        Lb = -10
        Ub = 10
        nd = 2
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = -186.73
        globalMin += Tol
    elif benchmark_number == 12:
        Lb = -10
        Ub = 10
        nd = 4
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 13:
        Lb = 0
        Ub = np.pi
        nd = 5
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = -4.687658
        globalMin += Tol
    elif benchmark_number == 14:
        Lb = -5
        Ub = 10
        nd = 10
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 15:
        Lb = 0
        Ub = np.pi
        nd = 10
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = -9.660151715641349
        globalMin += Tol
    elif benchmark_number == 16:
        Lb = -5.12
        Ub = 5.12
        nd = 30
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 17:
        Lb = -100
        Ub = 100
        nd = 30
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 18:
        Lb = -10
        Ub = 10
        nd = 30
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 19:
        Lb = -1.28
        Ub = 1.28
        nd = 30
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 20:
        Lb = -10
        Ub = 10
        nd = 30
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 21:
        Lb = -100
        Ub = 100
        nd = 30
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 22:
        Lb = -30
        Ub = 30
        nd = 30
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 23:
        Lb = -10
        Ub = 10
        nd = 30
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 24:
        Lb = -5.12
        Ub = 5.12
        nd = 30
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 25:
        Lb = -600
        Ub = 600
        nd = 30
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol
    elif benchmark_number == 26:
        Lb = -32
        Ub = 32
        nd = 30
        Lb = np.ones(nd) * Lb
        Ub = np.ones(nd) * Ub
        globalMin = 0
        globalMin += Tol

    return globalMin, Lb, Ub, nd, max_limit
