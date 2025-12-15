export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeObj = newGrades.filter((grade) => grade.studentId === student.id);
      const grade = gradeObj.length > 0 ? gradeObj[0].grade : 'N/A';
      return {
        ...student,
        grade,
      };
    });
}
