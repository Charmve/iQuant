load("@rules_python//python:defs.bzl", "py_binary", "py_test")
load("@third_party//:requirements.bzl", "requirement")

# TODO(https://github.com/bazelbuild/bazel-bench/issues/36): Make these work for python3.
py_binary(
    name = "qbot",
    srcs = ["qbot_main.py"],
    deps = [
        "//utils",
        requirement("wxPython"),
        requirement("pandas"),
        requirement("matplotlib"),
        requirement("backtrader"),
        requirement("backtrader_plotting"),
        requirement("scipy"),
        requirement("statsmodels"),
        requirement("quantstats"),
        requirement("requests"), # 这是yahoofinance需要
        requirement("loguru"), # 简化logger的使用
        requirement("binance-connector"),
        requirement("numba"), # pandas 多序列rolling需要
        requirement("pykalman"),
        requirement("tables"),
        requirement("scikit-learn"),
        requirement("empyrical"),
        requirement("stable-baselines3"),
        requirement("jupyter"),
        requirement("gym[all]"),
        requirement("pyglet"),
        requirement("tensorboard"),
        requirement("tensortrade"),
        requirement("yfinance"),
        requirement("pandas_datareader"),
    ],
)

py_test(
    name = "qbot_test",
    srcs = ["qbot_test.py"],
    deps = [
        ":qbot",
        "//testutils",
        requirement("mock"),
    ],
)
