var app_view = new Vue({
    el: '#app',
    data: {
        showSignIn: true,
        showCreateAccount: false,
        showFeed: false,
        showMakeAPost: false,
        showLeaderboard: false,

        showNavbar: false,
        // noProfile: false,

        leaderboard: {
            sort_by: ["Name", "Distance", "Time", "Date"],
            sort_by_idx: 3,
            filter_by: ["Today", "Last Week", "Last Month", "Last 3 Months", "Last Year", "All Time"],
            filter_by_idx: 5,
            data: []
        },


        // Profile: "Profile",

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
        //feedArrayHARDCODE: [{ "username": "john", "runIMG": "./img/johnrunning.jpeg", "Caption": "1 mile run", "Distance": "1 mile", "Time": "30 minutes", "Date": "10/3/10", "Comments": "{'username': 'susan', 'comment': 'what a great run today!'}" }, { "username": "jack", "runIMG": "./img/jackrunning.jpeg", "Caption": "2 mile run", "Distance": "2 mile", "Time": "20 minutes", "Date": "10/10/10", "Caption": "1 mile run", "Distance": "1 mile", "Time": "30 minutes", "Date": "10/3/10", "Comments": "{'username': 'sam', 'comment': 'awesome!'}" }, { "username": "jill", "runIMG": "./img/jillrunning.jpeg", "Caption": "3 mile run", "Distance": "3 mile", "Time": "60 minutes", "Date": "10/3/21", "Caption": "1 mile run", "Distance": "1 mile", "Time": "30 minutes", "Date": "10/3/10", "Comments": "{'username': 'sara', 'comment': 'lookin' good!'}" }],
        feedArrayHARDCODE: [
            {
                "caption": "Had a great run today! Can't wait to get back out this weekend!",
                "created": "Mon, 15 Nov 2021 05:49:05 GMT",
                "distance": 2.9,
                "imageurl": "http://localhost:8080/api/v1/posts/c779560fd34245f0b3c0acbd6afda970.jpeg",
                "owner": "jack",
                "postid": 1,
                "time": 21.4
            },
            {
                "caption": "Got everyone out for a run today!",
                "created": "Mon, 15 Nov 2021 05:49:05 GMT",
                "distance": 3.2,
                "imageurl": "3ce034d523584fc4a095055c1950206c.jpeg",
                "owner": "jill",
                "postid": 2,
                "time": 22.3
            }
        ],

        feedArray: [],




    },

    methods: {
        /* removed temporarily
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
        */
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
            //this.noProfile = true;
            this.mounted();


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
                //this.noProfile = true;
                this.mounted();

            }


        },

        feedClick: function (event) {
            this.showFeed = true;
            this.showMakeAPost = false;
            this.showLeaderboard = false;
            // this.showProfile = false;
            this.mounted();

        },
        makeAPostClick: function (event) {
            this.showFeed = false;
            this.showMakeAPost = true;
            this.showLeaderboard = false;
            // this.showProfile = false;


        },
        leaderboardClick: function (event) {
            this.showFeed = false;
            this.showLeaderboard = true;
            this.showMakeAPost = false;
            //this.showProfile = false;

        },

        //button clicked to refresh the feed
        updateFeed: function (event) {

            //get the new data from the api
            this.mounted();


        },



        // Leaderboard
        get_sort_dropdown_class: function (idx) {
            if (idx == this.leaderboard.sort_by_idx) return "active";
            return "";
        },

        on_sort_dropdown_click: function (idx) {
            this.leaderboard.sort_by_idx = idx;
        },

        get_filter_dropdown_class: function (idx) {
            if (idx == this.leaderboard.filter_by_idx) return "active";
            return "";
        },

        on_filter_dropdown_click: function (idx) {
            this.leaderboard.filter_by_idx = idx;
        },

        //set the feed array from the api
        //called on load in
        async mounted() {
            axios

            const posts_promise = axios.get('http://localhost:8080/api/v1/posts/');

            posts_promise

                .then((response) => response.data)

                .then(data => this.feedArray = data)
                .then((data => console.log(data)))

                .catch((e) => console.log("get feed data catch"))
        },


    },

    computed: {
        sorted_leaderboard: function () {

            if (!this.leaderboard) return []

            let leaderboard = this.leaderboard;

            data = leaderboard.data;

            // Name
            if (leaderboard.sort_by_idx == 0)
                data.sort((a, b) => (a.owner > b.owner) ? 1 : -1)
            // Distance
            else if (leaderboard.sort_by_idx == 1)
                data.sort((a, b) => (a.distance > b.distance) ? 1 : -1)
            // Time
            else if (leaderboard.sort_by_idx == 2)
                data.sort((a, b) => (a.time > b.time) ? 1 : -1)
            // Date
            // TODO

            return data;
        }
    },

    mounted() {

        axios
            .get('http://localhost:8080/api/v1/leaderboard/')
            .then(response => (this.leaderboard.data = response.data.data))
            .catch((e) => console.log("Leaderboard API call ERROR"))

    }


})
