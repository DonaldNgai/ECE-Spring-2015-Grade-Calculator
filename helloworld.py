import time

class Marks(object):
	"""docstring for Marks"""
	def __init__(self, labMarks, midtermGrade,examGrade):
		self.labMarks = int(labMarks);
		self.midtermGrade = int(midtermGrade);
		self.examGrade = int(examGrade);
		self.CalculateWeights();
		

	def PrintAllGrades(self):
		print "\nLabs: ", self.labMarks, "\n";
		print "Midterm: ", self.midtermGrade, "\n";
		print "Exam: %d" % self.examGrade, "\n";


	def PrintAllWeights(self):
		print "\nLabs: ", self.labWeight, "\n";
		print "Midterm: ", self.midtermWeight, "\n";
		print "Exam: %.1f" % self.examWeight;

	def PrintFinalGrade(self):
		print "\nYour Final Grade is: %.2f" % self.finalGrade;

	def CalculateWeights(self):
		self.CalculateWeightOfLabs();
		self.CalculateWeightOfMidterm();
		self.CalculateWeightOfExam();

	def CalculateWeightOfLabs(self):
		self.labWeight = 0;
		if self.examGrade >= 60:
			self.labWeight = .30;
		elif self.examGrade >= 40:
			self.labWeight = (self.examGrade - 30)/100;
		else:
			self.labWeight = .10;

	def CalculateWeightOfMidterm(self):
		self.midtermWeight = .20;

	def CalculateWeightOfExam(self):
		self.examWeight = 1 - (self.labWeight + self.midtermWeight);

	def CalculateFinalGrade(self):
		self.finalGrade = (self.labWeight*self.labMarks 
		+ self.midtermWeight*self.midtermGrade 
		+ self.examWeight*self.examGrade);

	def CalculateMidtermNeededToPass(self,desiredGrade):
		needed = desiredGrade - (self.labWeight*self.labMarks + self.examWeight*self.examGrade)/self.midtermWeight;
		if self.midtermGrade:
			print "Your midterm mark was %d and you need a %d to get a final of %d" % (self.midtermGrade,needed,desiredGrade);
		else:
			print "You need to get a %d in your midterm to get a %d" % (needed,desiredGrade);

	def CalculateLabNeededToPass(self,desiredGrade):
		needed = desiredGrade - (self.midtermWeight*self.midtermGrade + self.examWeight*self.examGrade)/self.labWeight;
		if self.labMarks:
			print "Your overall lab mark was %d and you need a %d to get a final of %d" % (self.labMarks,needed,desiredGrade);
		else:
			print "You need to get a %d in your midterm to get a %d" % (needed,desiredGrade);

	def CalculateExamNeededToPass(self,desiredGrade):
		needed = desiredGrade - (self.labWeight*self.labMarks + self.midtermWeight*self.midtermGrade)/self.examWeight;
		if self.examGrade:
			print "Your exam mark was %d and you need a %d to get a final of %d" % (self.examGrade,needed,desiredGrade);
		else:
			print "With a exam mark greater than or equal to 60,"
			self.examGrade = 60;
			self.CalculateWeights();
			needed = desiredGrade - (self.labWeight*self.labMarks + self.midtermWeight*self.midtermGrade)/self.examWeight;
			print " you need to get a %d in your exam to get a %d\n" % (needed,desiredGrade);

			print "With a exam mark greater than or equal to 40 but less than 60,"
			self.examGrade = 40;
			self.CalculateWeights();
			needed = desiredGrade - (self.labWeight*self.labMarks + self.midtermWeight*self.midtermGrade)/self.examWeight;
			print " you need to get a %d in your exam to get a %d\n" % (needed,desiredGrade);

			print "With a exam mark greater than or equal to 60,"
			self.examGrade = 0;
			self.CalculateWeights();
			needed = desiredGrade - (self.labWeight*self.labMarks + self.midtermWeight*self.midtermGrade)/self.examWeight;
			print " you need to get a %d in your exam to get a %d\n" % (needed,desiredGrade);

def GetGrades():
	global labMarks
	global midtermGrade
	global examGrade

	print "Please Enter your overall lab grade";
	labMarks = raw_input() or 0;
	print "Please Enter your midterm grade";
	midtermGrade = raw_input() or 0;
	print "Please Enter your final exam grade";
	examGrade = raw_input() or 0;


#MAIN PROGRAM
print "Initializing Script";
GetGrades();
student = Marks(labMarks,midtermGrade,examGrade);
student.CalculateFinalGrade();

quit = False;
while not (quit):
	print """\nChoose an option
	\n1: Print All Grades
	\n2: Print the resulting weight of everything
	\n3: Print Your Final Grade
	\n4: Print The midterm mark needed to pass
	\n5: Print the overall lab mark needed to pass
	\n6: Print the exam mark needed to pass
	\nQ or q: Quit Program\n""";
	option = raw_input();
	if option.lower() == 'q': quit = True;
	else: 
		try: 
			option = int(option);

			if option == 1:student.PrintAllGrades()
			elif option == 2:student.PrintAllWeights()
			elif option == 3:student.PrintFinalGrade()
			elif option == 4:student.CalculateMidtermNeededToPass(50)
			elif option == 5:student.CalculateLabNeededToPass(50)
			elif option == 6:student.CalculateExamNeededToPass(50)
			

			print "Press enter to continue!";
			time.sleep(2);
			raw_input();

		except:
			print "Invalid Option!";
			time.sleep(2);

#CalculateFinalGrade(userInput);