

var app_view = new Vue({
    el: '#app',
    data: {
        showSignIn: true,
        showCreateAccount: false,
        showFeed: false,
        showMakeAPost: false,
        showLeaderboard: false,
        showProfile: false,


        Profile: "Profile",

        username: '',
        password: '',
        first_name: '',
        last_name: '',
        new_username: '',
        new_password: '',
        new_password_2: '',
        

    },

    methods: {

        //called when the profile button is clicked
        profileClick: function(event){

            //if the profile is currently being shown close it
            if(this.showProfile){
                this.showProfile = false;
                //show the feed
                this.showFeed = true;

            }
            else{
                //open the profile screen
                //hide and show the things we need and dont
                this.showProfile = true;
                this.showSignIn = false;
                this.showFeed = false;
                this.showCreateAccount = false;
                this.showMakeAPost = false;
                this.showLeaderboard = false;
            }

        }, //end profileClick function

        //called when user clicks sign in button
        signInButton: function(event){

            //CHECK WITH THE API IF THERE LOG IN IS CORRECT
            /*if(username wrong){
                alert("username or password incorrect, please try again");
            }*/

            //IF SUCCESS THEN GO TO FEED
            this.showFeed = true;
            this.showSignIn = false;


        },//end sign in button function

        //called when user clicks create account button
        createAccountButton: function(event){

            //first go to create an account screen
            this.showSignIn = false;
            this.showCreateAccount = true;



        },//end create account button





    },
    
    computed: {

    },

    mounted() {

    }
})