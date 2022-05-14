library(Nonpareil);
samples <- read.table('samples_nonpareil.txt', sep='\t', header=TRUE, as.is=TRUE);
attach(samples);
nps <- Nonpareil.set(file, col=color, labels=label, plot.opts=list(plot.observed=FALSE));
detach(samples);
summary(nps);
