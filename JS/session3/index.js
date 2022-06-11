// const input = prompt();
// if (input === "") {
//     console.log("입력값이 없습니다.");
// } else{
//     console.log(input);
// }

// const result = fetch("https://jsonplaceholder.typicode.com/posts/1");
// console.log(result);

// fetch("https://jsonplaceholder.typicode.com/posts/1")
//     .then(res => res.json())
//     .then(console.log);
// console.log('test');

// const me = {
//     name: "고채원",
//     age: 24,
//     gender: 'female',
// };

// const someone = {
//     name: "홍길동",
//     age: 25,
//     gender: 'male',
// };

// function addMilitaryStateIfMale(person) {
//     if (person.gender === 'male') {
//         person.militaryState = false;
//     }
// }

// addMilitaryStateIfMale(me);
// addMilitaryStateIfMale(someone);

// function parseBoolean(value) {
//     if (value === true) {
//         return "참";
//     } else if (value === false) {
//         return "거짓";
//     }
// }

// me.militaryState !== undefined && console.log(parseBoolean(me.militaryState));
// someone.militaryState !== undefined && console.log(parseBoolean(me.militaryState));


// const input = prompt();
// console.log(imput || "입력값이 없습니다.");

// const me = {
//     name: "고채원",
//     age: 24
// };

// const { name } = me;

// console.log(name);
// console.log(name);
// console.log(name);
// console.log(name);
// console.log(name);

// const me = {
//     name: "고채원",
//     age: 24
// };

// const militaryMe = {
//     ...me,
//     militaryState: false,
// }

// console.log(militaryMe);

// const animals = ["개", "고양이"];
// const anotherAnimals = [...animals, "참새"];

// console.log(anotherAnimals);

const me = {
    name: "고채원",
    age: 24,
    militaryState: false,
};

const { militaryState, ...another } =me;

console.log(another);

const numbers = [0, 1, 2, 3, 4, 5, 6];

const [zero, ...rest] = numbers;

console.log(rest); 