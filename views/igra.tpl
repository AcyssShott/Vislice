% import model
<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>
  <table>
  <tr>
        ><td>
         <h3> {{ igra.pravilni_del_gesla()}} </h3>
        </td>
      </tr>
      <tr>
        <td><h3>Neuspeli poskusi: </h3></td>
        <td>{{igra.nepravilni_ugibi() }}</td>
      </tr>

      % if poskus == model.ZMAGA or poskus == model.PORAZ :
      <form action="/igra/" method="post">
        <button type="submit">Nova igra</button>
      </form>

      % else:
      <tr>
            <form action="/igra/{{id_igre}}" method="post">
                 <input type="text" name="poskus">
                 <input type="submit" name="Ugibaj">
              </form>
      </tr>
      % end
    </table>

  <blockquote>
    {{igra.pravilni_del_gesla() }}
  </blockquote>

  <img src="img/10.jpg" alt="obesanje">

</body>

</html>