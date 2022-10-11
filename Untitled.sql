CREATE TABLE "customer" (
  "cu_id" SERIAL PRIMARY KEY,
  "name" text,
  "last_name" text
);

CREATE TABLE "address" (
  "add_id" SERIAL UNIQUE PRIMARY KEY,
  "str_numb" text,
  "str_name" text,
  "city" text
);

CREATE TABLE "credit_card" (
  "cc_id" SERIAL UNIQUE PRIMARY KEY,
  "card_number" integer,
  "exp_date" integer,
  "cvv_number" integer
);

CREATE TABLE "order" (
  "ord_id" SERIAL UNIQUE PRIMARY KEY,
  "item_id" integer,
  "quantity" integer,
  "order_date" datetime
);

CREATE TABLE "items" (
  "item_id" SERIAL UNIQUE PRIMARY KEY,
  "item_name" text,
  "item_description" text,
  "price" money
);

ALTER TABLE "address" ADD FOREIGN KEY ("add_id") REFERENCES "customer" ("cu_id");

ALTER TABLE "credit_card" ADD FOREIGN KEY ("cc_id") REFERENCES "customer" ("cu_id");

ALTER TABLE "order" ADD FOREIGN KEY ("ord_id") REFERENCES "customer" ("cu_id");

ALTER TABLE "order" ADD FOREIGN KEY ("item_id") REFERENCES "items" ("item_id");
