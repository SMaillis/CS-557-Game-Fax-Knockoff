
CREATE DATABASE ActivityAnswers;
USE ActivityAnswers;

CREATE TABLE USERS (
    user_id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    password VARCHAR(64) NOT NULL,

    PRIMARY KEY (user_id),
    UNIQUE (username),
    UNIQUE (email)
);

CREATE TABLE ADMIN (
    user_id INT NOT NULL,
    admin_level VARCHAR(30) NOT NULL,

    PRIMARY KEY (user_id),

    FOREIGN KEY (user_id)
        REFERENCES USERS(user_id)
);

CREATE TABLE REGULAR_USER (
    user_id INT NOT NULL,
    reputation INT NOT NULL,

    PRIMARY KEY (user_id),

    FOREIGN KEY (user_id)
        REFERENCES USERS(user_id)
);

CREATE TABLE GAME (
    game_id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(150) NOT NULL,
    platform VARCHAR(50) NOT NULL,
    release_year SMALLINT,
    views INT NOT NULL,

    PRIMARY KEY (game_id)
);

CREATE TABLE GUIDE (
    guide_id INT NOT NULL AUTO_INCREMENT,
    author_id INT NOT NULL,
    game_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    body TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    views INT NOT NULL,

    PRIMARY KEY (guide_id),

    FOREIGN KEY (author_id)
        REFERENCES USERS(user_id),

    FOREIGN KEY (game_id)
        REFERENCES GAME(game_id)
);

CREATE TABLE QUESTION (
    question_id INT NOT NULL AUTO_INCREMENT,
    author_id INT NOT NULL,
    game_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    body TEXT NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    likes INT NOT NULL,
    dislikes INT NOT NULL,
    views INT NOT NULL,

    PRIMARY KEY (question_id),

    FOREIGN KEY (author_id)
        REFERENCES USERS(user_id),

    FOREIGN KEY (game_id)
        REFERENCES GAME(game_id)
);

CREATE TABLE ANSWER (
    answer_id INT NOT NULL AUTO_INCREMENT,
    question_id INT NOT NULL,
    author_id INT NOT NULL,
    body TEXT NOT NULL,
    is_accepted BOOLEAN NOT NULL,
    created_at TIMESTAMP NOT NULL,
    likes INT NOT NULL,
    dislikes INT NOT NULL,

    PRIMARY KEY (answer_id),

    FOREIGN KEY (question_id)
        REFERENCES QUESTION(question_id),

    FOREIGN KEY (author_id)
        REFERENCES USERS(user_id)
);

CREATE TABLE COMMENT (
    comment_id INT NOT NULL AUTO_INCREMENT,
    author_id INT NOT NULL,
    question_id INT NOT NULL,
    answer_id INT,
    body TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    likes INT NOT NULL,
    dislikes INT NOT NULL,

    PRIMARY KEY (comment_id),

    FOREIGN KEY (author_id)
        REFERENCES USERS(user_id),

    FOREIGN KEY (question_id)
        REFERENCES QUESTION(question_id),

    FOREIGN KEY (answer_id)
        REFERENCES ANSWER(answer_id)
);
