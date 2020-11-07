load("@rules_python//python:defs.bzl", "py_library")
load("@video_editor_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "video_editor_lib",
    srcs = glob(["*.py"]),
    deps = [
        requirement("imageio"),
        requirement("imageio-ffmpeg"),
        requirement("moviepy"),
        requirement("mss"),
        requirement("opencv-python"),
        requirement("pep8"),
        requirement("pylint"),
        requirement("pyscreenshot"),
        ]
)
