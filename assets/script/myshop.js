class myShop{

    constructor(data) {
        var myshop_id;
        var board_list;
        var board_title;
        var board_id;
        var board_desc;
        var board_th_url;
        var pcs_list;
        var pcs_image;
        var pcs_name;
        var result;
        var status;  

        this.myshop_id = data.myshop_id;
        this.board_title = data.board_title;
        this.board_id = data.board_id;
        this.board_desc = data.board_desc;
        this.pcs_list = data.pcs_list;
        this.pcs_image = data.pcs_image;
        this.pcs_name = data.pcs_name;
        this.status = data.status;
    }


   //이사님이 그때 알려주셨는데 뭐였지😭 렌더링!! 
    viewBoardInfo(){
        const list =$('.board-list');
        list.empty();
        result.board_list.forEach(item => {
            const li = $('<li></li>');
            const hashtags = item.board_desc.map(tag => `<a href=""><span class="item-des">#${tag}</span></a>`).join('');
            li.html(`
                <div class="item">
                    <a href=""><div class="item-thumbnail"><img src="${board_th_url}" alt="${item.board_id}"></div></a>
                    <a href=""><h6 class="item-name">${item.name}</h6></a>
                    <div class="item-hashtag">
                        ${hashtags}
                    </div>
                </div>

            `)


        })
        return`
        <li>
            <div class="item">
                <a href=""><div class="item-thumbnail"></div></a>
                <a href=""><h6 class="item-name">${board_title}</h6></a>
                <div class="item-hashtag">
                <a href="">
                    ${board_desc.map(item =>
                        `<span class="item-des">#${item}</span>`
                    ).join('')} <!-- 배열을 문자열로 변환 -->
                </a>
                </div>
            </div>
        </li>
        `
    }
  




}