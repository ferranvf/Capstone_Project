create table CourseCatalog (
  course_catalog_id integer primary key,
  college text,
  departement text,
  style text,
  course_level integer,
  course_number integer,
  course_name text,
  course_description text, 
  number_credits integer,
  requisits text
);

create table Course (
  course_id integer primary key,
  course_number integer,
  CRN integer,
  year_ integer,
  semester text,
  intructorID integer
);

create table Topics (
  topic_id integer primary key,
  parent text,
  topic_level integer,
  shortname text,
  topic_description text,
  course_id integer
);

create table LearningObjectives (
  learning_objective_id integer primary key,
  shortdescription text,
  longdescription text,
  topic_id integer,
  lo_source text,
  lo_references text,
  prerequisits text
)


