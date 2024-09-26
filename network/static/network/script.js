let currentPage = 'allPostsPage'

const getUsers = async () => {
  const response = await fetch('/users', { method: 'GET' })
  const users = await response.json()
}

const likeOrUnlikePost = async (user, postID) => {
  console.log(user, postID)
}

const getPosts = async () => {
  const response = await fetch('/posts', { method: 'GET' })
  const posts = await response.json()

  const postList = document.querySelector('#postList')

  posts.posts.forEach(post => {
    console.log(post)
    const listItem = document.createElement('li')

    listItem.classList = 'list-group-item post p-3'

    listItem.innerHTML = `
    <h3>${post.poster_name}</h3>
    <br>
    <button class="button btn-primary">Edit</button>
    <p class="">${post.content}</p>
    <p class="text-muted">${post.date}</p>
    <p id='likeButton' onclick="likeOrUnlikePost(${posts.user}, ${post.id})">${
      post?.liked_by?.includes(posts.user) ? '❤️' : '🖤'
    } ${post.liked_by ? len(post.liked_by) : '0'}</p>
    <button class="button btn-dark">comment</button>
    `
    postList.appendChild(listItem)
  })
}

const createPost = async event => {
  event.preventDefault()
  const content = document.querySelector('#postContent').value
  const body = JSON.stringify({ content })
  const token = event.target['csrfmiddlewaretoken'].value
  const response = await fetch('/posts', {
    method: 'POST',
    body: body,
    headers: { 'X-CSRFToken': token },
  })
  const newPost = await response.json()
  console.log(newPost)
  // If error dont update posts
  if (newPost.error) {
    document.querySelector('#error').innerHTML = newPost.error
  } else {
    // no error, get all new posts and put them on the page
    document.querySelector('#error').innerHTML = ''
    getPosts()
  }
}

const setCurrentPage = page => {
  currentPage = page

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

document.querySelector('#newPostForm').addEventListener('submit', e => {
  createPost(e)
})

document.addEventListener('DOMContentLoaded', e => {
  currentPage == 'allPostsPage' && getPosts()
})
