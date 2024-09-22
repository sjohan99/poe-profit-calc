export type CenterContentProps = {
  children: React.ReactNode;
  background?: string;
  className?: string;
  no_pad_children?: boolean;
};

export function CenterContent(props: CenterContentProps) {
  const extra_styling = props.className ?? "";
  return (
    <div className={`flex justify-center ${extra_styling}`.trim()}>
      <div className="min-w-20 flex-none -lg:min-w-0"></div>
      <div
        className={`max-w-screen-2xl grow rounded-sm ${props.background ?? ""}`.trim()}
      >
        <div
          className={`${props.no_pad_children ? "-lg:px-4" : "px-4"} py-3`.trim()}
        >
          {props.children}
        </div>
      </div>
      <div className="min-w-20 flex-none -lg:min-w-0"></div>
    </div>
  );
}
