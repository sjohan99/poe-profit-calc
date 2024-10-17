export type CenterContentProps = {
  children: React.ReactNode;
  background?: string;
  className?: string;
};

export function CenterContent(props: CenterContentProps) {
  const extra_styling = props.className ?? "";
  return (
    <div className={`flex justify-center ${extra_styling}`.trim()}>
      <div className="flex-none -lg:min-w-0"></div>
      <div
        className={`max-w-screen-2xl grow rounded-sm ${props.background ?? ""}`.trim()}
      >
        <div className={"px-3 py-3"}>{props.children}</div>
      </div>
      <div className="flex-none -lg:min-w-0"></div>
    </div>
  );
}
