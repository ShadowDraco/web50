let currentPage = 'allPostsPage'

const setCurrentPage = page => {
  currentPage = page
  console.log(page)
  switch (page) {
    case 'followingPage':
      document.querySelector('#allPostsPage').hidden = true
      document.querySelector('#followingPage').hidden = false
      document.querySelector('#profilePage').hidden = true
      break
    case 'profilePage':
      document.querySelector('#allPostsPage').hidden = true
      document.querySelector('#followingPage').hidden = true
      document.querySelector('#profilePage').hidden = false
      break
    default:
      document.querySelector('#allPostsPage').hidden = false
      document.querySelector('#followingPage').hidden = true
      document.querySelector('#profilePage').hidden = true
  }
}

document.querySelector('#nav-network').addEventListener('click', () => {
  setCurrentPage('allPostsPage')
})
document.querySelector('#nav-allPosts').addEventListener('click', () => {
  setCurrentPage('allPostsPage')
})
document.querySelector('#nav-following').addEventListener('click', () => {
  setCurrentPage('followingPage')
})
document.querySelector('#nav-user').addEventListener('click', () => {
  setCurrentPage('profilePage')
})
