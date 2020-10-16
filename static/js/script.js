var app = new Vue({
    el: "#app",
    delimiters: ["<%","%>"],
    data: {
        currentpage: null,
        onLine: 0,
        socket: io(),
        typing: null,
        typing_timeout:null,
        partner_timeout: null,
        partner: null,
        partner_ip: null,
        connected: null,
        new_user: {
            status: "Stop",
            code: 0
        },
        status: "Searching stranger...",
        message: "",
        chat_messages:[],
        three_dot_menu:false,
        yesNoModal:{
            title:"",
            show: false,
            subtitle: "",
            buttons:{
                type: 2,
                lables: ['Yes', 'No']
            },
            para:[],
            method: null
        }
    },
    updated() {
        this.scrollToBottom();
    },
    watch: {},
    mounted: function() {
        console.log("Vue2 mounted");
        this.currentpage = 'Home';
        this.connected = true;
        document.addEventListener('keydown', this.universalEvents.bind(this));
        this.configureSocket();
    },
    methods: {
// page change functions
        changePage(page){
            switch (page) {
                case "Home":
                    this.currentpage = page;
                    break;
                case "Chat":
                    this.currentpage = page;
                    this.searchUser();
                    break;
            }
        },
// Socket configurations
        configureSocket(){
            this.socket.io.autoConnect = false;
            this.socket.io._reconnectionAttempts = 0;
            self = this;
            this.socket.on('message', function(data) {
                if (data['from'] == self.partner){
                    clearTimeout(self.typing_timeout);
                    data['from'] = "stranger";
                    self.typing = "";
                    self.chat_messages.push(data);
                }
            });
            
            this.socket.on('online',function(data){
                self.onLine = data;
            });

            this.socket.on("partner", function(data){
                clearTimeout(self.partner_timeout);
                self.status = "You are talking to random stranger. Happy chatting! 😊";
                self.partner = data.sid;
                self.partner_ip = data.ip;
                self.chat_messages = [];
                self.new_user.status = "Stop";
                self.new_user.code = 0;
            });

            this.socket.on('disconnect', function(){
                self.partner = null;
                clearTimeout(self.partner_timeout);
                self.connected = false;
                self.status = "Server disconnected. Try reloading the page!";     
            });
            this.socket.on('typing', function(){
                if(self.partner){
                    clearTimeout(self.typing_timeout);
                    self.typing = "Stranger is typing...";
                    self.typing_timeout = setTimeout(()=>{self.typing = "";}, 2000);
                }
            });
            
            this.socket.on('leave_room',function(){
                self.status = "Stranger left the room. Press on new button to start search.";
                self.partner = null;
                self.new_user.status = "New";
                self.new_user.code = 2;
            });

            this.socket.on('keys',function(data){
                console.log(data);
            });

            this.socket.on('reload', function(){
                window.location.reload();
            });

            this.socket.on('redirect', function(data){
                window.location.replace(data.location);
            });

        },

// Socket functions
        searchUser(){
            if(this.connected){
                this.partner = null;
                clearTimeout(this.partner_timeout);
                this.status = "Searching stranger...";
                this.socket.emit('partner');
                this.partner_timeout = setTimeout(()=>{ this.status = "TTS could not find stranger for you. Try again later."; this.socket.emit('stop_search'); this.new_user.status = "New"; this.new_user.code = 2; }, 10000);
            }
        },
        sendmsg(){
            if( this.partner != null && this.connected){
                if (this.message){
                    json = {
                            "message":this.message, 
                            "to": this.partner,
                            "from": this.socket.io.engine.id
                        }
                    this.socket.emit('message',json);
                    json['from'] = "self";
                    self.new_user.status = "Stop";
                    self.new_user.code = 0;
                    this.chat_messages.push(json);
                    this.message = "";
                    }
            }
        },
        changeUserStatus(){
            if (this.connected){
                switch(this.new_user.code){
                    case 0:
                        this.new_user = { status: "Sure?", code: 1 };
                        break;
                    case 1:
                        this.new_user = { status: "New", code: 2 };
                        this.status = "You left the chat";
                        this.partner = null;
                        this.socket.emit('leave_room',{"partner": this.partner});
                        break;
                    case 2:
                        this.new_user = { status: "Searching..", code: -1 };
                        this.searchUser();
                        break
                }
            }
        },

//  Event functions
        inputBoxEvents(event){
            switch(event.key){
                case "Enter":
                    this.sendmsg();
                    break;
                default:
                    this.socket.emit("typing", {"partner": this.partner});
                    break;
            }
        },
        universalEvents(events){
            switch(event.key){
                case "Escape":
                    this.changeUserStatus();
                    break;
            }
        },

// Popups and menus
        handle2buttonPopup(){
            switch(this.yesNoModal.method){
                case 0 :
                    this.reportStranger();
                    break;
            }
        },
        reset2btnModal(){
            this.yesNoModal={
                title: "Do you want to report stranger?",
                show: false,
                para:[this.chat_messages],
                method: null
            }
        },
        showDotMenu(){
            if(this.partner_ip && this.connected){
                if(!this.three_dot_menu)
                    document.getElementsByClassName("dot-menu")[0].style.visibility = 'visible';
                else
                    document.getElementsByClassName("dot-menu")[0].style.visibility = 'hidden';
                this.three_dot_menu = !this.three_dot_menu;
            }
        },

// api calls
        reportStranger(){
            url = "/api/report";
            data = JSON.stringify({
                ip: this.partner_ip,
                chat: this.chat_messages
            });
            self = this;
            response =  apiCall(url, "POST", data);
            response.then(data =>{
                if(data.status="failure"){
                    this.yesNoModal={
                        title:data.message,
                        show: true,
                        subtitle: "",
                        para:[],
                        method: null,
                        buttons:{
                            type: 1,
                            lables: ["Okay"]
                        }
                    }
                }
            });
        },

// Other functions
        scrollToBottom() {
            try{
                let element = (document.getElementById("panelbody"));
                element.scrollTop = element.scrollHeight;
            }
            catch(err){}
        },
        confirmReport(){
            if(this.connected){
                this.showDotMenu();
                this.yesNoModal.title = "Do you want to report stranger? ";
                this.yesNoModal.subtitle = "This conversation will be analysed.";
                this.yesNoModal.method = 0;
                this.yesNoModal.show = true;
                this.yesNoModal.buttons = {
                    type: 2,
                    lables: ['Yes', 'No']
                };
            }
            else{
                document.getElementsByClassName("dot-menu")[0].style.visibility = 'hidden';
                this.three_dot_menu = !this.three_dot_menu;
            }
        },
    },
    beforeDestroy() {
        this.socket.disconnect();
        this.socket.close();
    },
});
