// declare controlled elements
const countHeading = document.getElementById('search-counter');
const quoteHeading = document.getElementById('random-quote');
const imfeelingluckyButton = document.getElementById('imfeelingluckyButton')
const searchbar = document.getElementById('search-bar')

// create lists to use for im feeling lucky

const randomAdjectves = [
    'funny',
    'sad',
    'cool',
    'interesting',
    'long'
]

const randomNouns = [
    'movies',
    'books',
    'storys',
    'poems',
    'animals',
    'foods',
    'restaurants',
    'meals',
    'games',
    'video games',
    'programs',
    'magazines'
]

// get the global page visits from count api
const getSearchCount = async () => {
    const response = await fetch('https://api.counterapi.dev/v1/freegooglesearchfrontend/searchcount/up')
    const data = await response.json()
    
    countHeading.innerText = `All time searches: ${data.count.toString()}`
}

// get random quote from dummyjason api
const getQuote = async () => {
   const response = await fetch('https://dummyjson.com/quotes/random')
   const data = await response.json()
   
   quoteHeading.innerText = `${data.quote} - ${data.author}`
}

// fake data for testing
const countdata = { count: 25};
countHeading.innerText = `All time searches: ${countdata.count.toString()}`
const quotedata = { quote: 'My name is Naruto Uzumaki and Im gonna be hokage', author: 'Naruto Uzumaki'}
quoteHeading.innerText = `${quotedata.quote} - ${quotedata.author}`

// logic for im feeling lucky
function imFeelingLucky(e) {
    
    const adj = randomAdjectves[Math.floor(Math.random() * randomAdjectves.length)]
    const noun = randomNouns[Math.floor(Math.random() * randomNouns.length)]
    // set value to search bar which is about to be submitted
    searchbar.value = `${adj} ${noun}`
}

// execute functions on page load
getSearchCount();
getQuote();
