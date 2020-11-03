Markov decision-making task, originally used in Tanaka et al. (2006),
then adopted by Neir Eshel and Niall Lally.
This was completely rewritten, extended and translated to German in 
March 2015 by Daniel Renz, renz@biomed.ee.ethz.ch.

The task consists of three parts:
1) Transition training, file "pruneTrain1.m"
2) Reward training, file "pruneTrain2.m"
3) Task "pruneTaskMRI.m"

While the task can be performed in the MRI scanner, the training can and 
should be performed outside, as it is time-intensive. Each training 
continues until the participants have an error rate of less than 10 
percent or a maximum training duration is reached. An absolute minimum of 
10 minutes per training phase is recommended. This, and other parameters 
(scanner port, object scaling, inputs etc) can be specified in the 
file "getParams.m". 


VERBALE ANLEITUNG
-----------------

Nach X/2 von insgesamt X Minuten im zweiten Training, wenn es Probleme mit dem Erlernen der Transitionsmatrize gibt:

"Es gibt in jedem Rechteck zwei Möglichkeiten, sich zu bewegen. Eine der beiden Aktionen bringt Sie immer entgegen dem Uhrzeigersinn im Kreis entlang zu dem nächsten Rechteck. Die zweite Aktion stellt im Vergleich dazu eine Abkürzung durch die Mitte dar, z.B. können Sie sich von links oben durch die Mitte hindurch nach rechts unten bewegen. Versuchen Sie sich also für jedes Rechteck zu merken, mit welcher Taste Sie sich im Kreis bewegen können, bzw. zu welchem anderen Rechteck sie gelangen können, wenn Sie die jeweils andere Taste drücken. Die Bewegungen durch die Mitte sind wie folgt (mit Gebärden zeigen): Von rechts oben können Sie nach links unten kommen, von links oben nach rechts unten (also überkreuz). Von links kommen Sie nach rechts, und von rechts nach links. Von unten links geht es gerade nach oben und von unten rechts ebenfalls gerade nach oben. Bitte versuchen Sie das jetzt weiter."

Nach dem zweiten Training sollte man vielleicht sogar allen Teilnehmern noch einmal folgendes sagen, nur um sicher zu gehen:

"Sie haben in dem zweiten Training ein paar Aufgaben testweise so gelöst, wie Sie das auch im Scanner machen sollen. Wir wollen Sie noch einmal explizit darauf hinweisen, um Missverständnissen vorzubeugen, dass Sie bei jeder dieser Aufgaben 9 Sekunden Zeit zum Überlegen haben, bevor Sie mit der Eingabe Ihrer Zugfolge beginnen. Falls Sie bei den einfacheren Aufgaben eventuell schon vor Ablauf der 9 Sekunden mit dem Überlegen fertig sind, können Sie dann sofort mit der Eingabe beginnen, ohne das Ende des Countdowns abwarten zu müssen. In jedem Fall, egal ob Sie abkürzen oder nicht, haben Sie aber nur insgesamt 2,5 Sekunden Zeit für die Eingabe. Diese Eingabe-Zeit beginnt entweder nach Ablauf des Countdowns, oder sobald Sie eine Taste drücken, je nachdem was als Erstes passiert."