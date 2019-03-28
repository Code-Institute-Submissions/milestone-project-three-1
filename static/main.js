var lives = 3;

function submitAnswer(answer) {

    var realAnswer = answer.toLowerCase();
    var userAnswer = $('#answer').val().toLowerCase();

    if (realAnswer != userAnswer) {

        lives--;
        
        document.getElementById('wrong-answer').classList.add('alert');
        document.getElementById('wrong-answer').classList.add('alert-danger');
        document.getElementById('wrong-answer').innerText = "Incorrect: " + userAnswer;

        if (lives == 0) {
            //redirect reset
            alert('No lives remaining! Better luck next time!');
            $(location).attr('href', '/gameover')
            return false;
        }
        else {
            alert('Wrong answer! You have ' + lives + ' remaining!');
            return false;
        }

    }
    else {
        return true;
    }
}