create table CourseCatalog (
  course_catalog_id integer(10) primary key,
  college text,
  department text,
  style text,
  course_type text,
  course_level integer(10),
  course_number integer(10),
  course_name text,
  course_description text, 
  number_credits integer(10),
  requisits text,
  degree_id integer(10),
  prerequisits nvarchar(100),
  year_taken integer(10),
  semester_taken nvarchar(100),
  restriction_id integer(10)
);

create table Course (
  course_id integer(10) primary key,
  course_number integer(10),
  CRN integer(10),
  year_ integer(10),
  semester nvarchar(100),
  instructorID integer(10)
);

create table Topics (
  topic_id integer(10) primary key,
  source_topic nvarchar(100),
  type_topic nvarchar(100),
  parent nvarchar(100),
  topic_level integer(10),
  shortname nvarchar(100),
  topic_description nvarchar(1000),
  course_id integer(10)
);

create table LearningObjectives (
  learning_objective_id integer(10) primary key,
  shortdescription nvarchar(100),
  longdescription nvarchar(1000),
  topic_id integer(255),
  topic_level_name nvarchar(1000),
  notes nvarchar(1000),
  lo_source text,
  lo_references nvarchar(100),
  prerequisits nvarchar(100)
);

create table Degrees (
	degree_id integer(50) primary key,
    degree_name nvarchar(100),
    degree_type nvarchar(100),
    degree_description nvarchar(1000),
    TotalCredits integer(10),
    credits_fall_1 integer(10),
    credits_spring_1 integer(10),
    credits_fall_2 integer(10),
    credits_spring_2 integer(10),  
    credits_fall_3 integer(10),
    credits_spring_3 integer(10),
    credits_fall_4 integer(10),
    credits_spring_4 integer(10)
);

create table CourseRestrictions (
	restriction_id integer(50) primary key,
	number_credits 	integer(10),
	parent_id integer(50),
    restriction_description nvarchar(100),
    parent_description nvarchar(100)
);
