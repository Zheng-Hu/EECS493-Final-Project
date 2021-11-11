

var app_view = new Vue({
    el: '#app',
    data: {
        showSignIn: true,
        showCreateAccount: false,
        showFeed: false,
        showMakeAPost: false,
        showLeaderboard: false,
        showProfile: false,

        showNavbar: false,

        noProfile: false,


        Profile: "Profile",

        username: '',
        password: '',
        keep_me_signed_in: false,
        first_name: '',
        last_name: '',
        new_username: '',
        new_password: '',
        new_password_2: '',

        Success: "btn-success",
        Normal: "btn-primary",

        //HARD CODED FEED DATA
        feedArray: [{ "username": "john", "runIMG": "./johnrunning.jpeg", "Caption": "1 mile run", "Distance": "1 mile", "Time": "30 minutes", "Date": "10/3/10", "Comments": "{'username': 'susan', 'comment': 'what a great run today!'}" }, { "username": "jack", "runIMG": "./jackrunning.jpeg", "Caption": "2 mile run", "Distance": "2 mile", "Time": "20 minutes", "Date": "10/10/10", "Caption": "1 mile run", "Distance": "1 mile", "Time": "30 minutes", "Date": "10/3/10", "Comments": "{'username': 'sam', 'comment': 'awesome!'}" }, { "username": "jill", "runIMG": "./jillrunning.jpeg", "Caption": "3 mile run", "Distance": "3 mile", "Time": "60 minutes", "Date": "10/3/21", "Caption": "1 mile run", "Distance": "1 mile", "Time": "30 minutes", "Date": "10/3/10", "Comments": "{'username': 'sara', 'comment': 'lookin' good!'}" }],

        heartImage: ['./heartNOFill.png', './heartNOFill.png', './heartNOFill.png'],
        noFillHeart: "./heartNOFill.png",
        heartFill: "./heartFill.png",

        postLiked: [false, false, false],

        Comment: [false, false, false],

        user_comment: [],

        showCommentsBox: [false, false, false],


    },

    methods: {

        //called when the profile button is clicked
        profileClick: function (event) {

            //if the profile is currently being shown close it
            if (this.showProfile) {
                this.showProfile = false;
                //show the feed
                this.showFeed = true;
                this.showNavbar = true;

            }
            else {
                //open the profile screen
                //hide and show the things we need and dont
                this.showProfile = true;
                this.showSignIn = false;
                this.showFeed = false;
                this.showCreateAccount = false;
                this.showMakeAPost = false;
                this.showLeaderboard = false;
                this.showNavbar = true;
            }

        }, //end profileClick function

        //called when user clicks sign in button
        signInButton: function (event) {

            //CHECK WITH THE API IF THERE LOG IN IS CORRECT
            /*if(username wrong){
                alert("username or password incorrect, please try again");
            }*/

            //IF SUCCESS THEN GO TO FEED
            this.showFeed = true;
            this.showSignIn = false;
            this.showNavbar = true;
            this.noProfile = true;


        },//end sign in button function

        //called when user clicks create account button
        createAccountButton: function (event) {

            //first go to create an account screen
            this.showSignIn = false;
            this.showCreateAccount = true;
        },//end create account button

        //calls when they create the accout
        createAccountButton_2: function (event) {

            //first check that the password is the same
            if (this.new_password != this.new_password_2) {
                alert("Passwords do not match please try again");
                return;
            }

            else {

                //call to api to get the account created


                //if account is successfully created
                this.showCreateAccount = false;
                this.showFeed = true;
                this.showNavbar = true;
                this.noProfile = true;

            }


        },

        feedClick: function (event) {
            this.showFeed = true;
            this.showMakeAPost = false;
            this.showLeaderboard = false;
            this.showProfile = false;

        },
        makeAPostClick: function (event) {
            this.showFeed = false;
            this.showMakeAPost = true;
            this.showLeaderboard = false;
            this.showProfile = false;


        },
        leaderboardClick: function (event) {
            this.showFeed = false;
            this.showLeaderboard = true;
            this.showMakeAPost = false;
            this.showProfile = false;

        },

        showComments: function (index) {

            if (this.showCommentsBox[index] == false) {
                this.$set(this.showCommentsBox, index, true);
            }
            else {
                this.$set(this.showCommentsBox, index, false);
            }


        },

        likePost: function (index) {
            //post is not liked so like the post
            if (this.postLiked[index] == false) {
                this.postLiked[index] = true;
                this.$set(this.heartImage, index, this.heartFill);
            }
            else {
                this.postLiked[index] = false;
                this.heartImage[index] = this.noFillHeart;
                this.$set(this.heartImage, index, this.noFillHeart);
            }


        },

        commentPost: function (index) {

            if (this.Comment[index] == false) {
                this.$set(this.Comment, index, true);
            }
            else {
                this.$set(this.Comment, index, false);
            }


        },

        postComment: function (index) {

            //add the comment to the comment box
            //set to the index of the input which is user_comment

            this.$set(this.Comment, index, false);

        }





    },

    computed: {

    },

    mounted() {

    }
})