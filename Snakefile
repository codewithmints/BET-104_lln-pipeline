configfile: "config.yaml"


rule all:
    input:
        "results/plot.png"


rule generate_data:
    output:
        "results/data.csv"
    params:
        n=config["n"],
        k_values=config["k_values"],
        repeats=config["repeats"]
    script:
        "scripts/generate_data.py"


rule plot:
    input:
        "results/data.csv"
    output:
        "results/plot.png"
    params:
        n=config["n"]
    script:
        "scripts/plot.py"
