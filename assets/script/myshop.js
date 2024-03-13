class myShop {
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
    var myResult;

    // this.myshop_id = data.myshop_id;
    // this.board_title = data.board_title;
    // this.board_id = data.board_id;
    // this.board_desc = data.board_desc;
    // this.pcs_list = data.pcs_list;
    // this.pcs_image = data.pcs_image;
    // this.pcs_name = data.pcs_name;
    // this.status = data.status;
  }

  //이사님이 그때 알려주셨는데 뭐였지😭 렌더링!!
  viewBoardInfo(result) {
    const list = $(".board-list ul");
    list.empty();
    result.board_list.forEach((item) => {
      const li = $("<li></li>");
      const hashtags = item.board_desc.map((tag) => `<a href=""><span class="item-des">#${tag}</span></a>`).join("");

      // 이미지 URL을 item 객체에서 정확히 참조합니다.
      li.html(`
                <div class="item">
                    <a href=""><div class="item-thumbnail"><img src="${item.board_th_url}" alt="${item.board_id}"></div></a>
                    <a href=""><h6 class="item-name">${item.board_title}</h6></a>
                    <div class="item-hashtag">
                        ${hashtags}
                    </div>
                </div>
            `);
      list.append(li);
    });
  }

  //   삭제예정
  getRandomColor() {
    let letters = "BCDEF".split("");
    let color = "#";
    for (let i = 0; i < 3; i++) {
      color += letters[Math.floor(Math.random() * letters.length)];
    }
    return color;
  }
  setGradientBackground() {
    const color1 = this.getRandomColor();
    const color2 = this.getRandomColor();
    const color3 = this.getRandomColor();
    const color4 = this.getRandomColor();
    const gradientStyle = `linear-gradient(-45deg, ${color1}, ${color2}, ${color3}, ${color4})`;

    $("body").css({
      background: gradientStyle,
      backgroundSize: "400% 400%",
    });
  }

  scrollMove() {
    $(".board-items ul").prepend("<li>" + item + "</li>");
    $(".board-items").animate({ scrollTop: 0 }, "slow");
  }

  // ====================================
  // ==============Ajax==================
  // ====================================

  getBoard_list() {
    var myResult;
    $.ajax({
      url: "./data/dummy.json",
      type: "GET",
    })
      .done((data) => {
        myResult = data;
        // console.log(myResult);
        this.viewBoardInfo(myResult);
        return myResult;
      })
      .fail(function (xhr, status, error) {
        console.error("AJAX 요청 실패: ", status, error);
      });
  }
}
let my_ginshop = new myShop();

$(document).ready(function () {
  const menu_btn = $(".menu-btn");
  menu_btn.on("click", function () {
    my_ginshop.getBoard_list();
  });

  //   ====삭제예정=======
  my_ginshop.setGradientBackground();
  my_ginshop.setInterval(setGradientBackground, 150);
});
