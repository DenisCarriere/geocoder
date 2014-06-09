-- Table: public.points

-- DROP TABLE public.points;

CREATE TABLE public.points
(
  gid integer NOT NULL DEFAULT nextval('points_gid_seq'::regclass),
  name character varying(80),
  geom geometry(Point,4326),
  CONSTRAINT points_pkey PRIMARY KEY (gid)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.points
  OWNER TO postgres;
