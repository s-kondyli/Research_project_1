library(Nonpareil);
x <- c('mg.r1_653AF_nonpareil.npo','mg.r1_1042E_nonpareil.npo','mg.r1_1042F_nonpareil.npo','mg.r1_1042G_nonpareil.npo','mg.r1_1042GFJE_nonpareil.npo');
labels <- c('653AF','1042E','1042E','1042F','1042G','1042GFJE');
color <- c("aquamarine","blueviolet","blue","brown1","chocolate","darkgray");
nps <- Nonpareil.set(x, labels = labels, col = color, plot.opts=list(plot.observed=FALSE, model.lwd=2));
summary(nps);
