rule example:
    output:
        os.path.join(dirs["results"], "example.done")
    conda:
        os.path.join(dirs["envs"], "example.yaml")
    benchmark:
        os.path.join(dirs["bench"], "example.txt")
    log:
        os.path.join(dirs["logs"], "example.err")
    script:
        os.path.join(dirs["scripts"], "example.py")
