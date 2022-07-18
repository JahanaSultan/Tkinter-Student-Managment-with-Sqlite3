import sqlite3


def s_login(username, password):
    conn = sqlite3.connect('student.db')
    data = conn.execute("""select st.f_name, st.l_name, st.s_number, 
                    st.p_number, st.email
                    from students st
                    join student_login sl
                    on st.s_number=sl.student_id
                    where st.email=? and sl.password=?""", (username, password))
    info = data.fetchall()
    conn.close()
    return info


def s_marks(student_id):
    conn = sqlite3.connect('student.db')
    data = conn.execute("""select lesson_name,  mark, date_mark
                        from lessons
                        join marks
                        using(lesson_id)
                        join students
                        using(s_number)
                        where s_number=?
                        order by date_mark desc
                      """, (student_id,))
    info = data.fetchall()
    conn.close()
    return info


def avarage(student_id):
    conn = sqlite3.connect('student.db')
    data = conn.execute("""select round(avg(mark),2)
                        from marks
                        where s_number=?""", (student_id,))
    info = data.fetchall()
    conn.close()
    return info


def t_login(username, password):
    conn = sqlite3.connect('student.db')
    data = conn.execute("""select teacher_name, teacher_surname,teacher_id
                    from teachers 
                    join teacher_login 
                    using(teacher_id)
                    where teacher_email=? and teacher_password=?""", (username, password))
    info = data.fetchall()
    conn.close()
    return info


def groups(id):
    conn = sqlite3.connect('student.db')
    data = conn.execute("""select goup_name
                       from teachers
                       join groups
                       using(teacher_id)
                       where teacher_id=?""", (id,))
    info = data.fetchall()
    conn.close()
    return info


def list_student(group_name):
    conn = sqlite3.connect('student.db')

    data = conn.execute("""select f_name || ' ' || l_name fullname, s_number
                        from students
                        join groups
                        using(group_id)
                        where goup_name=?
                        """, (group_name,))
    info = data.fetchall()
    conn.close()
    return info


def add_mark(s_id, mark):
    conn = sqlite3.connect('student.db')

    try:

        conn.execute("insert into marks(lesson_id,s_number,mark) values((select lesson_id from teachers join students using(teacher_id) where s_number=?), ?, ?)",
                     (s_id, s_id, mark))

        conn.commit()

        return True

    except sqlite3.IntegrityError or sqlite3.OperationalError:

        return False

    finally:
        conn.close()


def update_mark(mark, student_id, date):
    conn = sqlite3.connect('student.db')
    conn.execute("""update marks
                    set mark=?
                    where s_number=? and date_mark=?
                    """, (mark, student_id, date))
    conn.commit()
    conn.close()


def teacher_id(group_name):
    conn = sqlite3.connect('student.db')
    data = conn.execute(""" select teacher_id
                            from teachers
                            join groups
                            using(teacher_id)
                            where goup_name=?""", (group_name,))
    info = data.fetchall()
    conn.close()
    return info

def group_name(student_id):
    conn = sqlite3.connect('student.db')
    data = conn.execute(""" select goup_name
                            from groups
                            join students
                            using(group_id)
                            where s_number=?""", (student_id,))
    info = data.fetchall()
    conn.close()
    return info

def admin_login(username,password):
    conn = sqlite3.connect('student.db')
    data = conn.execute("""select username
                    from admin
                    where username=? and password=?""", (username, password))
    info = data.fetchall()
    conn.close()
    return info

def student_register(name,surname,s_number,p_number,email, group, password):

    conn=sqlite3.connect('student.db')
    

    try:

     conn.execute("""insert into students values(?,?,?,?,?,(select teacher_id from teachers join groups using(teacher_id) where goup_name=?),(select group_id from groups where goup_name=?))
    """,(name,surname,s_number,p_number,email,group,group))
     conn.commit()
     conn.execute("insert into student_login values(?,?)",(s_number,password))
     conn.commit()

     return True

    except sqlite3.IntegrityError or sqlite3.OperationalError:

        return False

    finally:
        conn.close()

def teacher_register(name, surname, teacher_id, email, lesson, password):
    conn=sqlite3.connect('student.db')
    

    try:

     conn.execute("""insert into teachers values(?,?,?,?,(select lesson_id from lessons where lesson_name=?))
    """,(name,surname,int(teacher_id), email,lesson))
     conn.commit()
     conn.execute("insert into teacher_login values(?,?)",(teacher_id,password))
     conn.commit()

     return True

    except sqlite3.IntegrityError or sqlite3.OperationalError:

        return False

    finally:
        conn.close()

def group_register(id, name, tname,tsurname):
    conn=sqlite3.connect('student.db')
    

    try:

     conn.execute("""insert into groups values(?,?,(select teacher_id from teachers where teacher_name=? and teacher_surname=?))
    """,(id,name,tname,tsurname))
     conn.commit()

     return True

    except sqlite3.IntegrityError or sqlite3.OperationalError:

        return False

    finally:
        conn.close()


def lesson_register(id, name):
    conn=sqlite3.connect('student.db')
    

    try:

     conn.execute("""insert into lessons values(?,?)
    """,(id,name))
     conn.commit()

     return True

    except sqlite3.IntegrityError or sqlite3.OperationalError:

        return False

    finally:
        conn.close()