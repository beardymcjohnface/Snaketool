
def main(**kwargs):
    open(kwargs["output"], "w").close()


if __name__ == "__main__":
    main(output=snakemake.output[0],)
