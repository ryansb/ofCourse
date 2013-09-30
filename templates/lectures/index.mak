<%inherit file="../master.mak" />

<div class='hero-unit'>
  <h1>LN</h1>
  <p>Lecture Notes: Agenda-y type things to keep the train on the tracks</p>
</div>
<div class="row-fluid">
    <div class="span4">
        <ul class="unstyled">
            <li><h2>Notes</h2></li>
            % for lecture in lectures:
              <li><a href="/lectures/${lecture.split('.')[0]}">Week ${lecture[1]} - Class
              ${lecture[3]}</a></li>
            % endfor
        </ul>
    </div>
</div>
