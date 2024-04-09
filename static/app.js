$(document).ready(function () {
  function loadCupcakes() {
    axios
      .get("/api/cupcakes")
      .then(function (response) {
        $(".cupcakes-list").empty();
        response.data.cupcakes.forEach((cupcake) => {
          $(".cupcakes-list").append(`
                        <div>
                            <p>Flavor: ${cupcake.flavor}</p>
                            <p>Size: ${cupcake.size}</p>
                            <p>Rating: ${cupcake.rating}</p>
                            <img src="${cupcake.image}" alt="Cupcake Image">
                        </div>
                    `);
        });
      })
      .catch(function (error) {
        console.error("Error loading cupcakes: ", error);
      });
  }

  loadCupcakes();

  $("#cupcake-form").submit(function (event) {
    event.preventDefault();
    const flavor = $("#flavor").val();
    const size = $("#size").val();
    const rating = $("#rating").val();
    const image = $("#image").val();

    axios
      .post("/api/cupcakes", {
        flavor: flavor,
        size: size,
        rating: rating,
        image: image,
      })
      .then(function (response) {
        console.log("Cupcakes added:", response.data);
        loadCupcakes();
      })
      .catch(function (error) {
        console.error("Error adding cupcake: ", error);
      });
  });
});
