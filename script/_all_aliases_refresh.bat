REM =========================
REM  �ꊇ�C���X�N���v�g
REM =========================

cmd /c sushi
ruby script/markdownlink_creator.rb
ruby script/fshalias_creator.rb
ruby script/specialurls_creator.rb
pause