use rand::{self, Rng};
use std::io::{self, Write};

fn main() {
    let words = vec!["rust", "mémoire", "sécurité", "performance"];
    let secret_word = words[rand::rng().random_range(0..words.len())];

    let mut guessed_letters = Vec::new();
    let mut attempts = 6;
    let mut revealed_letters = vec!['_'; secret_word.len()];

    while attempts > 0 && revealed_letters.contains(&'_') {
        show_word(&revealed_letters);
        println!("Essais restants : {}", attempts);
        print!("Entrez une lettre : ");
        io::stdout().flush().expect("flush failed");

        let guess = read_stdin();

        if guessed_letters.contains(&guess) {
            println!("Vous avez déjà proposé cette lettre.");
            continue;
        }

        guessed_letters.push(guess);

        if secret_word.contains(guess) {
            for (i, c) in secret_word.chars().enumerate() {
                if c == guess {
                    revealed_letters[i] = guess;
                }
            }
            println!("Bonne lettre !");
        } else {
            attempts -= 1;
            println!("Mauvaise lettre !");
        }
    }

    if revealed_letters.contains(&'_') {
        println!("Vous avez perdu ! Le mot était : {}", secret_word);
    } else {
        println!("Félicitations ! Vous avez deviné le mot : {}", secret_word);
    }

}

fn show_word(word: &Vec<char>) {
    print!("Mot : ");
    for c in word {
        print!("{c} ");
    }
    println!();
}

fn show_word_2(word: &Vec<char>) {
    print!("Mot : ");
    for (i, c) in word.iter().enumerate() {
        if i > 0 {
            print!(" ");
        }
        print!("{}", c);
    }
    println!();
}

fn read_stdin() -> char {
    let mut buf = String::new();
    loop {
        buf.clear();
        io::stdin().read_line(&mut buf).expect("read_line failed");
        let mut it = buf.trim().chars();
        match (it.next(), it.next()) {
            (Some(c), None) => return c, // exactement un scalaire Unicode
            _ => println!("Veuillez saisir une seule lettre."),
        }
    }
}
